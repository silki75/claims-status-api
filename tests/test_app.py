import sys
import os

sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), "../app")))

from app import app


def test_health():
    client = app.test_client()
    response = client.get("/health")
    assert response.status_code == 200
    assert response.json["status"] == "healthy"


def test_claim_status():
    client = app.test_client()
    response = client.get("/claims/12345")
    assert response.status_code == 200
    assert response.json["status"] == "Approved"