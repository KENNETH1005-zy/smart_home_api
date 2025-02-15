from fastapi.testclient import TestClient
from app.main import app

client = TestClient(app)

# Test User Registration
def test_register_user():
    response = client.post("/auth/register", json={
        "name": "John Doe",
        "email": "john@example.com",
        "password": "securepassword"
    })
    assert response.status_code == 200
    assert response.json()["message"] == "User registered successfully"

# Test User Login with Correct Credentials
def test_login_user():
    response = client.post("/auth/login", json={
        "email": "john@example.com",
        "password": "securepassword"
    })
    assert response.status_code == 200
    assert "access_token" in response.json()
    assert response.json()["token_type"] == "bearer"

# Test User Login with Wrong Credentials
def test_login_invalid_user():
    response = client.post("/auth/login", json={
        "email": "john@example.com",
        "password": "wrongpassword"
    })
    assert response.status_code == 401
    assert response.json()["detail"] == "Invalid credentials"