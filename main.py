from fastapi import FastAPI
from pydantic import BaseModel
from fastapi import Depends
from fastapi import status


# create the FastApi Application
app=FastAPI()

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