from fastapi import FastAPI
from pydantic import BaseModel

# create the FastApi Application
app=FastAPI()

# pydantic model for items
class Item(BaseModel):
    name:str
    description:str=None
    price:float
    tax:float=None


# define the route at the  home
@app.get('/')
def home():
    return {"message":"Testingggg"}

# create item
@app.post('/items')
async def create_item(item:Item):
    # print('iitem:--->>>',query,limit)
    return {'item_name':item.name,'price':item.price,'description':item.description,'tax':item.tax}