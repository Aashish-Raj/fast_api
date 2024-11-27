from fastapi import FastAPI
from pydantic import BaseModel
from fastapi import Depends
from fastapi import status
from fastapi.middleware.cors import CORSMiddleware
from  fastapi import Request
from fastapi.responses import JSONResponse


# create the FastApi Application
app=FastAPI()


#error  for 404
@app.exception_handler(404)
async def custom_404_error(request:Request,exc:Exception):
    return JSONResponse(
        status_code=404,
        content={'message':"The resource was not found"}
    )


# allowed origin
origins=[
    "http://localhost:8000",
]

# add cors middleware  to fast api
app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"], 
    allow_headers=["*"],

)

# pydantic model for items
class Item(BaseModel):
    name:str
    description:str=None
    price:float
    tax:float=None

# class dependecy  function
def get_query_param(query:str=None):
    print("calledd-->>>",query)
    return query



# define the route at the  home
@app.get('/')
def home():
    return {"message":"Testingggg"}

# create item
@app.post('/items',response_model=Item,status_code=status.HTTP_201_CREATED)
async def create_item(item:Item):
    # print('iitem:--->>>',query,limit)
    # return {'item_name':item.name,'price':item.price,'description':item.description,'tax':item.tax}
    return item


# add the  dependency in  fast api
@app.get('/read_items')
async def read_items(query:str=Depends(get_query_param)):
    return {'query_param':query}