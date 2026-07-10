from fastapi.testclient import TestClient
from main import app
import uuid

client = TestClient(app)


def create_test_user():
    return {
        "username": f"pytest_user_{uuid.uuid4()}",
        "password" : "password123"
    }

def get_auth_headers():
    user = create_test_user()

    register_response = client.post(
        "/register",
        json=user
    )
    assert register_response.status_code == 201

    login_response = client.post(
        "/login",
        data=user
    )
    assert login_response.status_code == 200

    token = login_response.json()["access_token"]

    return  {
        "Authorization": f"Bearer {token}"
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

    
    user = create_test_user()
    register_response = client.post(
        "/register",
        json=user

    )
    assert register_response.status_code == 201
    
    response = client.post(
        "/register",
        json=user
    )

    
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

def test_get_medicines_unauthorized():
    response = client.get("/medicines")

    assert response.status_code == 401
    assert response.json() == {
        "detail" : "Not authenticated"

    }

def test_get_medicine_authorized():
    from fastapi.testclient import TestClient
from main import app
import uuid

client = TestClient(app)


def create_test_user():
    return {
        "username": f"pytest_user_{uuid.uuid4()}",
        "password" : "password123"
    }

def get_auth_headers():
    user = create_test_user()

    register_response = client.post(
        "/register",
        json=user
    )
    assert register_response.status_code == 201

    login_response = client.post(
        "/login",
        data=user
    )
    assert login_response.status_code == 200

    token = login_response.json()["access_token"]

    return  {
        "Authorization": f"Bearer {token}"
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

    
    user = create_test_user()
    register_response = client.post(
        "/register",
        json=user

    )
    assert register_response.status_code == 201
    
    response = client.post(
        "/register",
        json=user
    )

    
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

def test_get_medicines_unauthorized():
    response = client.get("/medicines")

    assert response.status_code == 401
    assert response.json() == {
        "detail" : "Not authenticated"

    }

def test_get_medicine_authorized():
    user = create_test_user()
    register_response = client.post(
        "/register",
        json=user
    )
    assert register_response.status_code == 201
    
    login_response = client.post(
        "/login",
        data=user
    )
    assert login_response.status_code == 200

    token = login_response.json()["access_token"]
    headers = {
        "Authorization": f"Bearer {token}"
    }
    
    response = client.get(
        "/medicines",
        headers=headers
    )
    assert response.status_code == 200
    assert isinstance(response.json(), list)

def test_add_medicine():
    headers = get_auth_headers()

    medicine = {
    "name": f"pytest_name_{uuid.uuid4()}",
    "quantity": 100,
    "ndc": f"pytest_ndc_{uuid.uuid4()}"}

    response = client.post(
        "/medicines",
        json=medicine,
        headers = headers
    )
    assert response.status_code == 201
    assert response.json() == {"message": "Medicine added succesfully"}
    
def test_add_duplicate_ndc():
    headers=get_auth_headers()

    medicine = {
        "name" : "test_medicine",
        "quantity" : 100,
        "ndc" : f"pytest_ndc_{uuid.uuid4()}"
    }

    response = client.post(
        "/medicines",
        json=medicine,
        headers = headers
    )

    assert response.status_code == 201
    assert response.json() == {"message": "Medicine added succesfully"}

    duplidcate_response = client.post(
        "/medicines",
        json=medicine,
        headers = headers
    )
    assert duplidcate_response.status_code == 409
    assert duplidcate_response.json() == {"detail":"NDC already exists"}


def test_search_medicine():
    headers = get_auth_headers()

    medicine = {
        "name" : f"pytest_name_{uuid.uuid4()}",
        "quantity" : 100,
        "ndc" : f"pytest_ndc_{uuid.uuid4()}"
    }

    add_response = client.post(
        "/medicines",
        json=medicine,
        headers=headers
    )
    assert add_response.status_code == 201
    assert add_response.json() == {"message": "Medicine added succesfully"}

    search_response = client.get(
        f"/medicines/{medicine['name']}",
        headers=headers
    )

    assert search_response.status_code == 200
    
    assert search_response.json()["name"] == medicine["name"]
    assert search_response.json()["quantity"] == medicine["quantity"]
    assert search_response.json()["ndc"] == medicine["ndc"]
    

def test_search_missing_medicine():
    headers = get_auth_headers()

    search_response = client.get(
        "/medicines/fake_medicine",
        headers=headers
    )
    assert search_response.status_code == 404
    assert search_response.json() == {
        "detail" : "Medicine not found"
    }


def test_update_quantity():
    headers = get_auth_headers()

    medicine = {
        "name" : f"pytest_name_{uuid.uuid4()}",
        "quantity" : 100,
        "ndc" : f"pytest_ndc_{uuid.uuid4()}"
    }

    add_response = client.post(
        "/medicines",
        json=medicine,
        headers=headers
    )
    assert add_response.status_code == 201
    assert add_response.json() == {"message": "Medicine added succesfully"}

    update_quantity_response = client.put(
        f"/medicines/{medicine['name']}",
        json={"quantity" : 250},
        headers=headers
    )
    assert update_quantity_response.status_code == 200
    assert update_quantity_response.json()=={
        "message" : "Updated quantity"
    }

    search_response = client.get(
        f"/medicines/{medicine['name']}",
        headers=headers
    )

    assert search_response.status_code == 200
    assert search_response.json()['quantity'] == 250

    

def test_delete_medicine():
    headers = get_auth_headers()

    medicine = {
        "name" : f"pytest_name_{uuid.uuid4()}",
        "quantity" : 100,
        "ndc" : f"pytest_ndc_{uuid.uuid4()}"
    }

    add_response = client.post(
        "/medicines",
        json=medicine,
        headers = headers
    )
    assert add_response.status_code == 201
    assert add_response.json() == {"message": "Medicine added succesfully"}

    delete_response = client.delete(
        f"/medicines/{medicine['name']}",
        headers=headers
    )
    assert delete_response.status_code == 200
    assert delete_response.json() == {
    "message": "Medicine removed"}

    search_response = client.get(
    f"/medicines/{medicine['name']}",
    headers=headers)

    assert search_response.status_code == 404

    assert search_response.json() == {
    "detail": "Medicine not found"}


def test_delete_missing_medicine():
    headers = get_auth_headers()

    delete_response = client.delete(
        "/medicines/DNE",
        headers=headers
    )
    assert delete_response.status_code == 404
    assert delete_response.json() == {
    'detail' : "Medicine not found"}

    
    response = client.get(
        "/medicines",
        headers=headers
    )
    assert response.status_code == 200
    assert isinstance(response.json(), list)

def test_add_medicine():
    headers = get_auth_headers()

    medicine = {
    "name": f"pytest_name_{uuid.uuid4()}",
    "quantity": 100,
    "ndc": f"pytest_ndc_{uuid.uuid4()}"}

    response = client.post(
        "/medicines",
        json=medicine,
        headers = headers
    )
    assert response.status_code == 201
    assert response.json() == {"message": "Medicine added succesfully"}
    
def test_add_duplicate_ndc():
    headers=get_auth_headers()

    medicine = {
    "name": f"pytest_name_{uuid.uuid4()}",
    "quantity": 100,
    "ndc": f"pytest_ndc_{uuid.uuid4()}"
}

    response = client.post(
        "/medicines",
        json=medicine,
        headers = headers
    )

    assert response.status_code == 201
    assert response.json() == {"message": "Medicine added succesfully"}

    duplidcate_response = client.post(
        "/medicines",
        json=medicine,
        headers = headers
    )
    assert duplidcate_response.status_code == 409
    assert duplidcate_response.json() == {"detail":"NDC already exists"}


def test_search_medicine():
    headers = get_auth_headers()

    medicine = {
        "name" : f"pytest_name_{uuid.uuid4()}",
        "quantity" : 100,
        "ndc" : f"pytest_ndc_{uuid.uuid4()}"
    }

    add_response = client.post(
        "/medicines",
        json=medicine,
        headers=headers
    )
    assert add_response.status_code == 201
    assert add_response.json() == {"message": "Medicine added succesfully"}

    search_response = client.get(
        f"/medicines/{medicine['name']}",
        headers=headers
    )

    assert search_response.status_code == 200
    
    assert search_response.json()["name"] == medicine["name"]
    assert search_response.json()["quantity"] == medicine["quantity"]
    assert search_response.json()["ndc"] == medicine["ndc"]
    

def test_search_missing_medicine():
    headers = get_auth_headers()

    search_response = client.get(
        "/medicines/fake_medicine",
        headers=headers
    )
    assert search_response.status_code == 404
    assert search_response.json() == {
        "detail" : "Medicine not found"
    }


def test_update_quantity():
    headers = get_auth_headers()

    medicine = {
        "name" : f"pytest_name_{uuid.uuid4()}",
        "quantity" : 100,
        "ndc" : f"pytest_ndc_{uuid.uuid4()}"
    }

    add_response = client.post(
        "/medicines",
        json=medicine,
        headers=headers
    )
    assert add_response.status_code == 201
    assert add_response.json() == {"message": "Medicine added succesfully"}

    update_quantity_response = client.put(
        f"/medicines/{medicine['name']}",
        json={"quantity" : 250},
        headers=headers
    )
    assert update_quantity_response.status_code == 200
    assert update_quantity_response.json()=={
        "message" : "Updated quantity"
    }

    search_response = client.get(
        f"/medicines/{medicine['name']}",
        headers=headers
    )

    assert search_response.status_code == 200
    assert search_response.json()['quantity'] == 250

    

def test_delete_medicine():
    headers = get_auth_headers()

    medicine = {
        "name" : f"pytest_name_{uuid.uuid4()}",
        "quantity" : 100,
        "ndc" : f"pytest_ndc_{uuid.uuid4()}"
    }

    add_response = client.post(
        "/medicines",
        json=medicine,
        headers = headers
    )
    assert add_response.status_code == 201
    assert add_response.json() == {"message": "Medicine added succesfully"}

    delete_response = client.delete(
        f"/medicines/{medicine['name']}",
        headers=headers
    )
    assert delete_response.status_code == 200
    assert delete_response.json() == {
    "message": "Medicine removed"}

    search_response = client.get(
    f"/medicines/{medicine['name']}",
    headers=headers)

    assert search_response.status_code == 404

    assert search_response.json() == {
    "detail": "Medicine not found"}


def test_delete_missing_medicine():
    headers = get_auth_headers()

    delete_response = client.delete(
        "/medicines/DNE",
        headers=headers
    )
    assert delete_response.status_code == 404
    assert delete_response.json() == {
    'detail' : "Medicine not found"}
