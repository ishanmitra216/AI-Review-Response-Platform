import csv
from pathlib import Path

DATASETS_DIR = Path(__file__).parents[1] / "datasets"

SENTIMENT_DATASETS = [
    ("sentiment_dataset.csv", "sentiment", "review_text"),
    ("restaurant_reviews_dataset.csv", "sentiment", "review_text"),
    ("hotel_reviews_dataset.csv", "sentiment", "review_text"),
    ("review_response_pairs_dataset.csv", "sentiment", "review_text"),
]

print("Training sentiment model...")

all_rows = []
for filename, label_col, text_col in SENTIMENT_DATASETS:
    path = DATASETS_DIR / filename
    if path.exists():
        with open(path, newline="", encoding="utf-8") as f:
            reader = csv.DictReader(f)
            rows = [
                {"text": row[text_col], "label": row[label_col]}
                for row in reader
                if row.get(text_col) and row.get(label_col)
            ]
        print(f"Loaded {len(rows)} examples from {filename}")
        all_rows.extend(rows)
    else:
        print(f"Dataset not found: {filename}, skipping")

print(f"Total training examples: {len(all_rows)}")

# placeholder for actual training logic
print("(training logic not yet implemented)")