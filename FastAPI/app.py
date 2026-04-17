import uvicorn
from fastapi import fastapi

app=FASTAPI()

#get,post,update,delete - get is post data at backend but not secure,
#backend p
@app.get('/')
def index():
    return{'message':'hello students, how are you!'}

@app.get('/name')
def index():
    return{'message':'hello Mansi'}
# to run fastapi - uvicorn filename:objectname
@app.get('/{name}')
def getname(name:str):
    return{'Name is':f'{name}'}


if __name__ =='__main__':
    uvicorn.run(app,host='127.0.0.1', port =8000)