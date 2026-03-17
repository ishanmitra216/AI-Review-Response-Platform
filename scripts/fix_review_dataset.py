"""
Fix encoding corruption in review_dataset.csv.

Corruptions found:
- `?ÿ?ÿ` (0x3F 0xFF repeated) in product names — corrupted Unicode decorators
- `\x83??` before prices  — corrupted UTF-8 encoding of ₹ (U+20B9)
- Various lone control/high bytes (0x80-0x9F, 0xFF) — corrupted emojis/symbols
"""

import re
import csv
import io
from pathlib import Path

SRC = Path(__file__).parents[1] / "ai_models" / "datasets" / "review_dataset.csv"
DST = SRC  # overwrite in-place


def fix_corrupted(text: str) -> str:
    """Apply all fixes to latin-1-decoded text from the original corrupt file."""

    # 1. Restore rupee sign: \x83 followed by one or two `?` before a digit
    text = re.sub(r"\x83\?{1,2}(?=\d)", "₹", text)

    # 2. Remove `?ÿ` sequences (corrupted multi-byte Unicode, safe to strip)
    text = re.sub(r"\?ÿ", "", text)

    # 3. Remove all remaining non-ASCII bytes in U+0080-U+00FF range.
    #    After step 1 restored ₹ (U+20B9, outside this range), every
    #    remaining char in this band is corrupted emoji / symbol garbage.
    text = re.sub(r"[\x80-\xff]", "", text)

    # 4. Remove zero-width and BOM junk
    text = re.sub(r"[\u200b\u200c\u200d\ufeff]", "", text)

    # 5. Collapse runs of 2+ question marks — left-over replacement chars
    #    after stripping corrupt emoji bytes
    text = re.sub(r"\?{2,}", "", text)

    # 6. Trim stray whitespace introduced by removals above
    text = re.sub(r"  +", " ", text).strip()

    return text


def restore_rupee_symbol(text: str) -> str:
    """Re-add ₹ to price fields that lost it (e.g. after a double-process run)."""
    # Price fields look like: ,"3,999", or ,"12,999",
    # Only add ₹ when the field value starts directly with a digit
    return re.sub(r'(?<=,")([\d][,\d]+)(?=")', r"₹\1", text)


def main():
    print(f"Reading {SRC} ...")
    with open(SRC, "rb") as f:
        raw = f.read()

    # Detect encoding: if the file is valid UTF-8 already, only do a light pass
    try:
        text = raw.decode("utf-8")
        already_utf8 = True
        print("File is already valid UTF-8 — applying light-pass corrections ...")
    except UnicodeDecodeError:
        text = raw.decode("latin-1")
        already_utf8 = False
        print("Encoding corruption found — applying full fix ...")

    if already_utf8:
        # Only re-add ₹ if it was stripped by a previous bad run
        if '₹' not in text:
            print("  Rupee symbol missing — restoring ...")
            text = restore_rupee_symbol(text)
        # Still clean up any residual question-mark artefacts
        text = re.sub(r"\?{2,}", "", text)
        text = re.sub(r"  +", " ", text).strip()
    else:
        text = fix_corrupted(text)

    # Validate we can round-trip through the CSV parser cleanly
    reader = csv.DictReader(io.StringIO(text))
    rows = list(reader)
    print(f"Parsed {len(rows):,} data rows successfully")

    # Write back as clean UTF-8
    with open(DST, "w", encoding="utf-8", newline="") as f:
        f.write(text)

    print(f"Written clean UTF-8 file to {DST}")
    print("Preview of first 3 rows:")
    for row in rows[:3]:
        print(f"  ProductName : {row['ProductName'][:80]}")
        print(f"  Price       : {row['Price']}")
        print(f"  Rate        : {row['Rate']}")
        print(f"  Review      : {row['Review']}")
        print(f"  Summary     : {row['Summary']}")
        print()


if __name__ == "__main__":
    main()
