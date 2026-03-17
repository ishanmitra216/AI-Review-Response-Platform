"""
Fix sentiment_dataset.csv to align with the AI Review Response Platform project.

Changes applied:
1. Rename all Indonesian columns to English equivalents
2. Translate Indonesian categorical values to English
3. Add `sentiment` column derived from rating (1-2 → negative, 3 → neutral, 4-5 → positive)
4. Drop rows missing both review_text and rating (not usable for training)
5. Round delivery_distance_km to 2 decimal places
6. Write clean UTF-8 output
"""

import csv
import io
from pathlib import Path

SRC = Path(__file__).parents[1] / "ai_models" / "datasets" / "sentiment_dataset.csv"

COLUMN_MAP = {
    "ID_Pesanan":       "order_id",
    "Waktu_Transaksi":  "timestamp",
    "Kategori_Menu":    "menu_category",
    "Harga_Pesanan":    "order_price",
    "Jarak_Kirim_KM":   "delivery_distance_km",
    "Waktu_Tunggu_Menit": "wait_time_minutes",
    "Rating_Pelanggan": "rating",
    "Ulasan_Teks":      "review_text",
    "Status_Promo":     "promo_applied",
    "Tingkat_Keluhan":  "complaint_level",
    "Status_Pesanan":   "order_status",
}

COMPLAINT_MAP = {
    "Tidak Ada": "none",
    "Rendah":    "low",
    "Tinggi":    "high",
}

ORDER_STATUS_MAP = {
    "Selesai":    "completed",
    "Dibatalkan": "cancelled",
    "Refund":     "refund",
}


def rating_to_sentiment(rating_str: str) -> str:
    if not rating_str:
        return ""
    try:
        r = float(rating_str)
    except ValueError:
        return ""
    if r >= 4.0:
        return "positive"
    elif r >= 3.0:
        return "neutral"
    else:
        return "negative"


def main():
    print(f"Reading {SRC} ...")
    with open(SRC, encoding="utf-8", newline="") as f:
        reader = csv.DictReader(f)
        original_rows = list(reader)

    print(f"Original rows: {len(original_rows):,}")

    out_rows = []
    dropped = 0
    for row in original_rows:
        rating = row.get("Rating_Pelanggan", "").strip()
        text = row.get("Ulasan_Teks", "").strip()

        # Drop rows that have neither rating nor review text
        if not rating and not text:
            dropped += 1
            continue

        new_row = {}
        for old_col, new_col in COLUMN_MAP.items():
            val = row.get(old_col, "").strip()

            if new_col == "delivery_distance_km" and val:
                try:
                    val = f"{float(val):.2f}"
                except ValueError:
                    pass

            if new_col == "complaint_level":
                val = COMPLAINT_MAP.get(val, val)

            if new_col == "order_status":
                val = ORDER_STATUS_MAP.get(val, val)

            new_row[new_col] = val

        new_row["sentiment"] = rating_to_sentiment(rating)
        out_rows.append(new_row)

    fieldnames = list(COLUMN_MAP.values()) + ["sentiment"]

    buf = io.StringIO()
    writer = csv.DictWriter(buf, fieldnames=fieldnames, lineterminator="\r\n")
    writer.writeheader()
    writer.writerows(out_rows)
    content = buf.getvalue()

    with open(SRC, "w", encoding="utf-8", newline="") as f:
        f.write(content)

    print(f"Dropped rows (no text and no rating): {dropped:,}")
    print(f"Output rows: {len(out_rows):,}")
    print(f"Written to {SRC}")

    # Summary stats
    from collections import Counter
    sentiments = Counter(r["sentiment"] for r in out_rows if r["sentiment"])
    print(f"\nSentiment distribution: {dict(sorted(sentiments.items()))}")
    print(f"Rows with review_text: {sum(1 for r in out_rows if r['review_text']):,}")
    print(f"Rows with rating: {sum(1 for r in out_rows if r['rating']):,}")

    print("\nSample rows:")
    for r in out_rows[:3]:
        print(f"  order_id   : {r['order_id']}")
        print(f"  rating     : {r['rating']}")
        print(f"  review_text: {r['review_text']}")
        print(f"  sentiment  : {r['sentiment']}")
        print(f"  complaint  : {r['complaint_level']}")
        print(f"  status     : {r['order_status']}")
        print()


if __name__ == "__main__":
    main()
