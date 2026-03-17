import csv
from pathlib import Path

DATASETS_DIR = Path(__file__).parents[1] / "datasets"

TOPIC_DATASETS = [
    ("review_dataset.csv", "topics", "Review", "utf-8"),
    ("restaurant_reviews_dataset.csv", "topics", "review_text", "utf-8"),
    ("hotel_reviews_dataset.csv", "topics", "review_text", "utf-8"),
    ("review_response_pairs_dataset.csv", "topics", "review_text", "utf-8"),
]

print("Training topic model...")

all_rows = []
for filename, label_col, text_col, encoding in TOPIC_DATASETS:
    path = DATASETS_DIR / filename
    if path.exists():
        with open(path, newline="", encoding=encoding) as f:
            reader = csv.DictReader(f)
            rows = [
                {"text": row[text_col], "topics": row.get(label_col, "")}
                for row in reader
                if row.get(text_col)
            ]
        print(f"Loaded {len(rows)} examples from {filename}")
        all_rows.extend(rows)
    else:
        print(f"Dataset not found: {filename}, skipping")

print(f"Total training examples: {len(all_rows)}")

print("(training logic not yet implemented)")