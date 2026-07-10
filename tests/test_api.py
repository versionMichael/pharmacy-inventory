from fastapi.testclient import TestClient
from main import app
import uuid

client = TestClient(app)

def create_test_user():
    return {
        "username": f"pytest_user_{uuid.uuid4()}",
        "password" : "password123"
    }

def test_root():
    response = client.get("/")
    assert response.status_code == 200
    assert response.json() =={
        "message" : "Pharmacy Inventory API"
    }

def test_register_user():

    user = create_test_user()

    response= client.post("/register", json=user)

    assert response.status_code == 201

    assert response.json() == {
    "message": "User registered successfully"
}

def test_register_duplicate_user():

    #arrange
    user = create_test_user()
    register_response = client.post(
        "/register",
        json=user

    )
    assert register_response.status_code == 201
    # act
    response = client.post(
        "/register",
        json=user
    )

    #assert
    assert response.status_code == 409
    assert response.json() == {
        "detail" : "Username already taken"
    }


def test_login_success():

    user = create_test_user()

    register_response = client.post(
        "/register",
        json=user
    )
    assert register_response.status_code == 201

    response = client.post(
        "/login",
        data=user
    )

    assert response.status_code == 200
    assert response.json()["token_type"] == "bearer"
    assert response.json()["access_token"]

def test_invalid_password():
    user = create_test_user()
    register_response = client.post(
        "/register",
        json=user
    )
    assert register_response.status_code ==201

    response = client.post(
        "/login",
        data={
            "username": user["username"],
            "password" : "password1234"
        })
    assert response.status_code == 401
    assert response.json() == {
        "detail" : "Invalid username or password"
    }

def test_nonexistent_user():
    data = {
        "username" : "DNE",
        "password" : "password123"
    }
    response = client.post(
        "/login",
        data=data
    )
    assert response.status_code == 401
    assert response.json() == {
        "detail" : "Invalid username or password"
    }