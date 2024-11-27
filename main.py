from fastapi import FastAPI

# create the FastApi Application
app=FastAPI()



# define the route at the  home
@app.get('/')
def home():
    return {"message":"Testingggg"}