from fastapi.testclient import TestClient
from app.main import app

def test_health():
    assert TestClient(app).get("/health").status_code == 200

def test_run():
    response=TestClient(app).post("/v1/run",json={"value":"demo"})
    assert response.status_code == 200
