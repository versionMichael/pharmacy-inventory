from fastapi import FastAPI, HTTPException, Depends
import database
from pydantic import BaseModel, ConfigDict
from jose import jwt , JWTError
from auth import (
    hash_password,
    verify_password,
    create_access_token,
    oauth2_scheme,
    SECRET_KEY,
    ALGORITHM,
)
from fastapi.security import OAuth2PasswordRequestForm

app = FastAPI()

class MedicineCreate(BaseModel):
    name : str
    quantity: int
    ndc : str

class MedicineResponse(BaseModel):
    id: int
    name : str
    quantity: int
    ndc : str

    model_config = ConfigDict(from_attributes=True)


class QuantityUpdate(BaseModel):
    quantity : int

class UserCreate(BaseModel):
    username : str
    password : str


def get_current_user(token : str = Depends(oauth2_scheme)):
    credentials_exception = HTTPException(
    status_code = 401,
    detail="Could not validate credentials"
    )
    try:
        payload = jwt.decode(
            token,
            SECRET_KEY,
            algorithms=[ALGORITHM]
            )
        username = payload.get("sub")
        if username is None:
            raise credentials_exception
        
    except JWTError:
        raise credentials_exception
    
    user = database.get_user(username)

    if user is None:
        raise credentials_exception
    
    return user

@app.get("/")
def root():
    return {"message": "Pharmacy Inventory API"}



@app.get("/medicines", response_model=list[MedicineResponse])
def get_medicines(current_user= Depends(get_current_user)):
    return database.get_all_medicines()

@app.post("/medicines", status_code=201)
def add_medicine(medicine: MedicineCreate, current_user= Depends(get_current_user)):
    if database.ndc_exists(medicine.ndc):
        raise HTTPException(
            status_code=409,
            detail="NDC already exists"
        )
    database.add_medicine(medicine.name, medicine.quantity, medicine.ndc)
    return {"message": "Medicine added succesfully"}

@app.delete("/medicines/{name}")
def delete_medicine(name : str, current_user= Depends(get_current_user)):
    if database.remove_medicine(name):
        return{"message" : "Medicine removed"}
    raise HTTPException(
        status_code = 404,
        detail="Medicine not found"
    )

@app.get("/medicines/{name}", response_model=MedicineResponse)
def search_medicine(name : str, current_user= Depends(get_current_user)):
    medicine = database.search_medicine(name)
    if medicine is None:
        raise HTTPException(
            status_code=404,
            detail="Medicine not found"
        )
    
    return medicine

@app.put("/medicines/{name}")
def update_quantity(name : str, medicine: QuantityUpdate, current_user= Depends(get_current_user)):
    if database.update_quantity(name,medicine.quantity):
        return{"message" : "Updated quantity"}
    raise HTTPException(
        status_code=404,
        detail="Medicine not found"
    )

@app.post("/register", status_code=201)
def register(user : UserCreate):
    existing_user = database.get_user(user.username)

    if existing_user:
        raise HTTPException(
            status_code=409,
            detail="Username already taken"
        )
    hashed_password = hash_password(user.password)
    database.create_user(user.username, hashed_password)

    return {"message": "User registered successfully"}

@app.post("/login")
def login(user : OAuth2PasswordRequestForm = Depends()):
    existing_user = database.get_user(user.username)
    if not existing_user:
        raise HTTPException(
            status_code=401,
            detail= "Invalid username or password"
        )
    if not verify_password(user.password, existing_user.hashed_password):
        raise HTTPException(
    status_code=401,
    detail="Invalid username or password"
    )
    
    access_token = create_access_token(
        data={'sub': existing_user.username}
    )

    return {
        "access_token" : access_token,
        "token_type" : "bearer"
    }

