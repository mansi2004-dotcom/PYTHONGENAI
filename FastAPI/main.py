from fastapi import FastAPI,UploadFile
from pydantic import BaseModel
from typing import List,Optional 

app = FastAPI()

#Fake db
items_db = [{"Name":'ANaya',"Age":28,"City":"Banglore"},
{"Name":'Mansi',"Age":28,"City":"Banglore"},
{"Name":'Riya',"Age":28,"City":"Banglore"}
]
class Item(BaseModel):
    id:int
    name:str
    city:str
    description:Optional[str]=None



@app.get("/")
def read_root():
    return {"mesage":"Welcome to FASTAPI"}

@app.get("/items")
def read_items():
    return items_db

@app.get("/items/{item_id}")
def read_item(item_id:int):
    for item in items_db:
        if item["ID"]==item_id:
            return item
        raise HTTPException(status_code =404, detail="Item not Found")

@app.post("/add_item")
def create_item(item:Item):
    return item

@app.put("/update/{item_id}")
def update_item(item_id:int,item:Item):
    for i,db_item in enumerate(items_db):
        if db_item["ID"]==item_id:
            items_db[i]=item.dict()
            return{"message":"Item Updated Successfully"}
        raise HTTPException(Statud_code = 404, detail="Item not Found")

        
@app.delete("/delete/{item_id}")
def delete_data(item_id:int):
    for i,db_item in enumerate(items_db):
        if db_item["ID"]==item_id:
            del items_db[i]
            return{"message":"Item Deleted Successfully"}
        raise HTTPException(status_code=404, detail="Item not Found")

@app.post("/uploadfile/")
def create_upload_file(file:UploadFile(...)):
    return{"filename":file.filename,"content_type":file.content_type}


if __name__=="__main__":
    import uvicorn
    uvicorn.run(app,host="127.0.0.1",port=8000)

