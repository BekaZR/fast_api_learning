from fastapi import FastAPI
from pydantic import BaseModel, HttpUrl

app = FastAPI()


class Product(BaseModel):
    name: str
    description: str
    price: float
    
    class Config:
        orm_mode = True
        schema_extra = {
            "example": {
                "name": "MacBook",
                "description": "Best working notebook",
                "price": 1000.0
            }
        }


@app.post('/product/')
def create_product(product: Product):
    return product