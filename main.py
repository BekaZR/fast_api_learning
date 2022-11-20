from unicodedata import numeric
from fastapi import FastAPI
from pydantic import BaseModel

class Product(BaseModel):
    name: str
    price: int
    
app = FastAPI()

@app.post("/product/")
def create_product(product: Product):
    return product
