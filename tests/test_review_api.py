from fastapi.testclient import TestClient
from backend.app.main import app
import io

client = TestClient(app)


def test_analyze_review():
    # sentiment endpoint should return the correct polarity label
    payload = {"text": "I love this product"}
    resp = client.post("/reviews/analyze", json=payload)
    assert resp.status_code == 200
    body = resp.json()
    assert body["sentiment"] == "positive"


def test_upload_dataset(tmp_path):
    # create a small CSV file in memory and upload it
    csv_content = "col1,col2\n1,2\n"
    file_obj = io.BytesIO(csv_content.encode("utf-8"))
    files = {"file": ("test.csv", file_obj, "text/csv")}

    resp = client.post("/datasets/upload", files=files)
    assert resp.status_code == 200
    data = resp.json()
    assert "filename" in data and data["filename"] == "test.csv"
    # cleanup the file that was written
    import os
    os.remove(data["path"])
