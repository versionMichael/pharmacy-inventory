from fastapi.testclient import TestClient
from main import app

client = TestClient(app)

def test_root():
    response = client.get("/")
    assert response.status_code == 200
    assert response.json() =={
        "message" : "Pharmacy Inventory API"
    }

def test_register_user():

    #arrange
    user = {
        "username" : "testuser",
        "password" : "password123"
    }

    #act
    response = client.post(
        "/register",
        json=user
    )

    #assert
    assert response.status_code == 201
    assert response.json() =={
        "message": "User registered successfully"
    }