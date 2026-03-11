from fastapi import APIRouter, File, UploadFile, HTTPException
from pathlib import Path

# datasets are stored in the ai_models/datasets directory relative to the
# repository root.  ``__file__`` lives under backend/app/api so we need to go up
# three levels to reach the workspace root.
DATASET_DIR = Path(__file__).parents[3] / "ai_models" / "datasets"
DATASET_DIR.mkdir(parents=True, exist_ok=True)

router = APIRouter()


@router.post("/upload")
async def upload_dataset(file: UploadFile = File(...)):
    """Upload a CSV file and save it to the datasets directory.

    The frontend / operator can send a multipart/form-data request with a
    single ``file`` field. Only files ending in ``.csv`` are accepted.  The
    saved location is returned in the response.

    This makes it easy to populate ``review_dataset.csv`` or
    ``sentiment_dataset.csv`` with training data without having to clone the
    repository manually.
    """

    if not file.filename.lower().endswith(".csv"):
        raise HTTPException(status_code=400, detail="Only CSV files allowed")

    dest = DATASET_DIR / file.filename
    # write streamed contents to disk
    with open(dest, "wb") as f:
        f.write(await file.read())

    return {"filename": file.filename, "path": str(dest)}
