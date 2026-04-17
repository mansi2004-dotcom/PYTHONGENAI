# Section - A
from fastapi import FastAPI, HTTPException,UploadFile, File, Depends
from pydantic import BaseModel
from typing import List, Optional

app = FastAPI()

Info_db =[{"ID":1,"Name":"Mansi","Course":"Btech", "College":"SBBSU"}]

@app.get("/")
def read_root():
    return {"mesage":"Welcome to FASTAPI"}

@app.get("/About")
def read_Info():
    return Info_db

@app.get("/user/{user_id}")
def read_Info(Info_id:int):
    for info in Info_db:
        if Info["ID"]==Info_id:
            return Info
        raise HTTPException(status_code=404, detail="Info not Found")



@app.get("/search")
def search(q: str):
    return {"search_query": q}


# Section B
# @app.post("/add_Info")
# def create_Info(Info:Info):
#     return Info

#Request body model
class User(BaseModel):
    id:int
    name:str
    age:int
    city: str
#POST API
@app.post("/user")
def create_user(user: User):
    return{
        "name":user.name,
        "age":user.age,
        "city":user.city
    }

# pydantic model 
@app.post("/user")
def create_user(user:User):
    return user