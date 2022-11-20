from fastapi import FastAPI

app = FastAPI()


fake_product_db = [
    {
        "name": "Apple",
        "price": 12.2
        },
    {
        "name": "Box",
        "price": 11.2
        },
    {
        "name": "Phone",
        "price": 12222.2
        },
]

@app.get("/product/")
def get_product(skip: int = 0, limit: int = 2):
    return {"product": fake_product_db[skip : skip + limit]}
