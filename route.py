from fastapi import APIRouter
import datetime

route=APIRouter()

@route.post("/register")
def register(username:str,password:str):
    return {"username":username,"password":password}


@route.get("/wish")
def invite():
    current_time = datetime.datetime.now()
    hour = current_time.hour

    if 5 <= hour < 12:
        return {"message": "Good morning"}

    elif 12 <= hour < 17:
        return {"message": "Good afternoon"}

    elif 17 <= hour < 21:
        return {"message": "Good evening"}

    else:
        return {"message": "Good night"}
