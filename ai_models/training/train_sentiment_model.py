import csv
from pathlib import Path

DATA_PATH = Path(__file__).parents[1] / "datasets" / "sentiment_dataset.csv"

print("Training sentiment model...")

if DATA_PATH.exists():
    with open(DATA_PATH, newline="", encoding="utf-8") as f:
        reader = csv.reader(f)
        rows = list(reader)
    print(f"Loaded {len(rows)} examples from {DATA_PATH}")
else:
    print(f"No sentiment dataset found at {DATA_PATH}, skipping load")

# placeholder for actual training logic
print("(training logic not yet implemented)")