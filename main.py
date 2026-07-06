from fastapi import FastAPI, HTTPException
import database
from pydantic import BaseModel, ConfigDict


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

@app.get("/medicines", response_model=list[MedicineResponse])
def get_medicines():
    return database.get_all_medicines()

@app.post("/medicines", status_code=201)
def add_medicine(medicine: MedicineCreate):
    if database.ndc_exists(medicine.ndc):
        raise HTTPException(
            status_code=409,
            detail="NDC already exists"
        )
    database.add_medicine(medicine.name, medicine.quantity, medicine.ndc)
    return {"message": "Medicine added succesfully"}

@app.delete("/medicines/{name}")
def delete_medicine(name : str):
    if database.remove_medicine(name):
        return{"message" : "Medicine removed"}
    raise HTTPException(
        status_code = 404,
        detail="Medicine not found"
    )

@app.get("/medicines/{name}", response_model=MedicineResponse)
def search_medicine(name : str):
    medicine = database.search_medicine(name)
    if medicine is None:
        raise HTTPException(
            status_code=404,
            detail="Medicine not found"
        )
    
    return medicine

@app.put("/medicines/{name}")
def update_quantity(name : str, medicine: QuantityUpdate):
    if database.update_quantity(name,medicine.quantity):
        return{"message" : "Updated quantity"}
    raise HTTPException(
        status_code=404,
        detail="Medicine not found"
    )