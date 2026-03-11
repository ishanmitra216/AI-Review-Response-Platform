import csv
from pathlib import Path

DATA_PATH = Path(__file__).parents[1] / "datasets" / "review_dataset.csv"

print("Training topic model...")

if DATA_PATH.exists():
    with open(DATA_PATH, newline="", encoding="utf-8") as f:
        reader = csv.reader(f)
        rows = list(reader)
    print(f"Loaded {len(rows)} examples from {DATA_PATH}")
else:
    print(f"No review dataset found at {DATA_PATH}, skipping load")

print("(training logic not yet implemented)")