from sqlalchemy import create_engine, select, func
from sqlalchemy.orm import sessionmaker
from models import Base, Medicine, User
from dotenv import load_dotenv
import os

load_dotenv(override=False)


DATABASE_URL = os.getenv("DATABASE_URL")
engine = create_engine(DATABASE_URL)

Session = sessionmaker(bind=engine)
session = Session()

Base.metadata.create_all(engine)


def get_all_medicines():
    statement = select(Medicine)
    result = session.execute(statement)
    medicines = result.scalars().all()
    return medicines


def add_medicine(name, quantity, ndc):
    medicine = Medicine(name=name, quantity = quantity,ndc = ndc)
    session.add(medicine)
    session.commit()
    

def search_medicine(name):
    statement = select(Medicine).where(
         func.lower(Medicine.name) == func.lower(name))
    result = session.execute(statement)
    medicine = result.scalars().first()
    return medicine

def ndc_exists(ndc):
    statement = select(Medicine).where(Medicine.ndc == ndc)
    result = session.execute(statement)
    medicine = result.scalars().first()
    return medicine

def update_quantity(name, quantity):


    medicine = search_medicine(name)

    if medicine is None:
            return False

    medicine.quantity = quantity
    session.commit()
    return True

def remove_medicine(name):
    medicine = search_medicine(name)

    if medicine is None:
        return False

    session.delete(medicine)
    session.commit()
    return True

def create_user(username, hashed_password):
     user = User(
          username = username,
          hashed_password = hashed_password
     )
     session.add(user)
     session.commit()

def get_user(username):
     statement = select(User).where(
          func.lower(User.username)== func.lower(username)
          )
     result = session.execute(statement)
     user = result.scalars().first()
     return user