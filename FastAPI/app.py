import uvicorn
from fastapi import FastAPI
from input import getData, heartInput
import joblib

app=FASTAPI()
model = joblib.load('model.pkl')

#get,post,update,delete - get is post data at backend but not secure,
#backend p
@app.get('/')
def index():
    return{'message':'hello students, how are you!'}

@app.get('/name')
def index():
    return{'message':'hello Mansi'}
# to run fastapi - uvicorn filename:objectname
@app.get('/name')
def printnamm():
    return{'message':'hello Mansi'}

# #@app.get('/{name}')
# def getName(name:str):
#     return {"Name is":f'{name}'}

# @app.post('/{name}')
# def getName(name:str):
#     return {"name is":f'{name}'}

@app.post('/getname')
def getName(data:getData):
    dict_data=data.model_dump()
    print(dict_data)

    return dict_data


if __name__ =='__main__':
    uvicorn.run(app,host='127.0.0.1', port =8000)