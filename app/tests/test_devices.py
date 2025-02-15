from fastapi.testclient import TestClient
from app.main import app

client = TestClient(app)

def test_create_device():
    response = client.post("/devices/", json={"type": "Temperature Sensor", "room_id": 1})
    assert response.status_code == 200
    assert response.json()["type"] == "Temperature Sensor"

def test_get_device():
    response = client.get("/devices/1")
    assert response.status_code == 200