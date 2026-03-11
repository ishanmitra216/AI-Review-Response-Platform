from fastapi.testclient import TestClient
from backend.app.main import app
import os

client = TestClient(app)


def test_generate_response(monkeypatch):
    # Rather than exercise the real OpenAI client (which in recent versions
    # raises an error if you hit ``ChatCompletion``), monkeypatch the high‑level
    # ``generate_response`` helper that the endpoint calls.
    # the endpoint imports ``generate_response`` directly, so override the
    # reference in the router module rather than the helper module.
    import app.api.response_routes as rr

    def fake_generate(text):
        return "dummy reply"

    monkeypatch.setattr(rr, "generate_response", fake_generate)

    payload = {"text": "This is a review"}
    resp = client.post("/responses/generate", json=payload)
    assert resp.status_code == 200
    data = resp.json()
    assert data["response"] == "dummy reply"
