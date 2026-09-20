from fastapi import FastAPI
import json
from fastapi import Path
from fastapi import HTTPException
from fastapi import Query
from pydantic import BaseModel, AnyUrl, EmailStr, Field
from typing import List, Dict, Annotated, Literal, Optional
from fastapi.responses import JSONResponse
from fastapi import Form
from fastapi import Header
from fastapi import File, UploadFile
from fastapi import Depends
from fastapi.security import HTTPBearer,HTTPAuthorizationCredentials
from function import facto
from function import fibonacci
from route import route
from middle import Authmiddleware
from middle import ErrorHandlingmiddleware
from middle import Timingmiddleware
from middle import mymiddleware
from fastapi.middleware.cors import CORSMiddleware
from function import even
from function import odd
from function import table as table_func
from function import caheck_prime
from function import display_num
from function import display_even
from function import display_odd
from function import display_century
from function import table_of
from function import even_odd
from function import cube_n
from function import square_n
from function import call_factorial
from function import primine
from function import fibo
from function import dis
from function import dio
from function import deso
from function import oss
from function import evss

app=FastAPI()
security=HTTPBearer()

# app.add_middleware(Authmiddleware)
app.add_middleware(ErrorHandlingmiddleware)
app.add_middleware(Timingmiddleware)
app.add_middleware(mymiddleware)
app.add_middleware(CORSMiddleware,
allow_methods=["*"],
allow_headers=["*"],
allow_origins=["*"],
allow_credentials=True)

app.include_router(route)

def load_data():
    with open ("patient.json","r") as f:
        return json.load(f)

def save_data(data):
    with open ("patient.json","w") as f:
        return json.dump(data,f)

class Patient(BaseModel):
    id:Annotated[str,Field(...,description="Unique patient ID")]
    name:Annotated[str,Field(...,description="Patient name")]
    age:Annotated[int,Field(...,gt=0,le=120,description="Patient age")]
    height:Annotated[float,Field(...,gt=0,description="Height in cm")]
    weight:Annotated[float,Field(...,gt=0,description="Weight in kg")]
    BMI:Annotated[float,Field(...,gt=0,description="Body Mass Index")]
    gender:Annotated[Literal["Male","Female"],Field(...,description="Patient gender")]
    phone: Annotated[str, Field(..., min_length=10, max_length=15)]
    email:Annotated[EmailStr,Field(...,description="Patient email")]
    blood_group:Annotated[Literal["A+","A-","B+","B-","AB+","AB-","O+","O-"],Field(...,description="Blood group")]
    state:Annotated[str,Field(...,description="State")]
    city:Annotated[str,Field(...,description="City")]
    problem:Annotated[str,Field(...,description="Patient problem")]
    medical_history: Annotated[list[str], Field(default_factory=list, description="...")]
    url: Optional[AnyUrl] = None

class PatientUpdate(BaseModel):
    name:Annotated[Optional[str],Field(None,description="Patient name")]
    age:Annotated[Optional[int],Field(None,gt=0,le=120,description="Patient age")]
    height:Annotated[Optional[float],Field(None,gt=0,description="Height in cm")]
    weight:Annotated[Optional[float],Field(None,gt=0,description="Weight in kg")]
    BMI:Annotated[Optional[float],Field(None,gt=0,description="Body Mass Index")]
    gender:Annotated[Optional[Literal["Male","Female"]],Field(None,description="Patient gender")]
    phone:Annotated[Optional[str],Field(None,min_length=10,max_length=15)]
    email:Annotated[Optional[EmailStr],Field(None,description="Patient email")]
    blood_group:Annotated[Optional[Literal["A+","A-","B+","B-","AB+","AB-","O+","O-"]],Field(None,description="Blood group")]
    state:Annotated[Optional[str],Field(None,description="State")]
    city:Annotated[Optional[str],Field(None,description="City")]
    problem:Annotated[Optional[str],Field(None,description="Patient problem")]
    medical_history:Annotated[Optional[list[str]],Field(None,description="Medical history")]
    url:Annotated[Optional[AnyUrl],Field(None,description="Patient related URL")]



@app.get("/")
def root():
    return "Patient World"

@app.get("/about")
def about():
    return "This is all about Patient World"

@app.get("/greet")
def greet():
    return "Welcome to patients world"

@app.get("/view")
def view_all_patient():
    data=load_data()
    return data


@app.get("/view/{patient_id}")
def get_patient_id(patient_id:str=Path(...,description="getting  id of patient",examples="P001")):
    data=load_data()
    if patient_id in data:
        return data[patient_id]
    raise HTTPException(status_code=404,detail="patient not found")


@app.get("/sort")
def sort(sort_by:str=Query(...,description="Sort by patients age, height, weight"),order_by:str=Query(...,description="order by aescending or descending")):
    valid_domains=["age","height","weight"]
    if sort_by not in valid_domains:
        raise HTTPException(status_code=404,detail="patient not found")
    if order_by not in ["asc","desc"]:
        raise HTTPException(status_code=404,detail="patient not found")
    data=load_data()
    sorted_order=True if order_by=="desc" else False
    sorted_data=sorted(data.values(),key=lambda x:x.get(sort_by,0),reverse=sorted_order)
    return sorted_data

@app.post("/New")
def create_patient(patient:Patient):
    data=load_data()
    if patient.id in data:
        raise HTTPException(status_code=400,detail="patient already exists")
    data[patient.id]=patient.model_dump(mode="json",exclude={"id"})
    save_data(data)
    return JSONResponse(status_code=201,content="patient created")

@app.put("/update/{patient_id}")
def update_patient(update:PatientUpdate,patient_id:str=Path(...,description="update the existing patient")):
    data=load_data()
    if patient_id not in data:
        raise HTTPException(status_code=404,detail="patient not found")
    existing_user=data[patient_id]
    update_data=update.model_dump(mode="json",exclude_none=True)
    for key,value in update_data.items():
        existing_user[key]=value
    existing_user["id"]=patient_id
    update_patient_object=Patient(**existing_user)
    updated_patient=update_patient_object.model_dump(mode="json",exclude={"id"})
    data[patient_id]=updated_patient
    save_data(data)
    return JSONResponse(status_code=200,content="patient updated")


@app.delete("/delete/{patient_id}")
def delete(patient_id:str=Path(...,description="the patient deleted")):
    data=load_data()
    if patient_id not in data:
        raise HTTPException(status_code=404,detail="patient not found")
    del data[patient_id]
    save_data(data)
    return JSONResponse(status_code=200,content="patient deleted")


@app.post("/login")
def login(username:str=Form(...),password:str=Form(...),token=Depends(security)):
    return {"password":password,"username":username}

@app.get("/secure")
def secure(token:str=Header(...)):
    return {"token":token}


@app.post("/Upload")
def upload(file: UploadFile = File(...),token=Depends(security)):
     return {"filename":file.filename,"content_type":file.content_type}
    

@app.post("/get_current_user")
def get_current_user(token=Depends(security)):
    return {"token":token}


@app.post("/protected")
def protected(credentials:HTTPAuthorizationCredentials=Depends(security)):
    return {
        "credentials":credentials.credentials,
        "scheme":credentials.scheme
    }

@app.post("/factorial")
def factorial(n:int,token=Depends(security)):
    return facto(n)


@app.post("/fibonacci")
def fibo(n:int,token=Depends(security)):
    return fibonacci(n)


@app.get("/even_century")
def century():
    return even()


@app.post("/odd")
def odd_mine():
    return odd()

@app.post("/table")
def get_table(n: int):
    return table_func(n)

@app.post("/prime")
def prime(n:int):
     return caheck_prime(n)

@app.post("/display")
def display():
    return display_num()
    

@app.post("/de")
def de():
    return display_even()

@app.post("/do")
def do():
    return display_odd()

@app.post("/dc")
def dc():
    return display_century()


@app.post("/tn")
def tn(n:int):
    return table_of(n)

@app.post("/oe")
def oe(n:int):
    return even_odd(n)


@app.post("/cube")
def cube(n:int):
    return cube_n(n)

@app.post("/square")
def square(n:int):
    return square_n(n)


@app.post("/facto")
def facto(n:int):
    return call_factorial(n)

@app.post("/pri")
def prime_num(n:int):
    return primine(n)

@app.post("/fb")
def fibon(n:int):
    return fibo(n)

@app.post("/dis")
def di():
    return dis()


@app.post("/den")
def dev():
    return dio()

@app.post("/don")
def doo():
    return deso()


@app.post("/dos")
def dmm():
    return oss()


@app.post("/vss")
def ev():
    return evss()
