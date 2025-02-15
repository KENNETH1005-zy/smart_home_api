from fastapi.testclient import TestClient
from app.main import app

client = TestClient(app)

def test_create_house():
    response = client.post("/houses/", json={"name": "My Smart Home"})
    assert response.status_code == 200
    assert response.json()["name"] == "My Smart Home"

def test_get_house():
    response = client.get("/houses/1")
    assert response.status_code == 200