from fastapi import FastAPI, HTTPException
from model import Item
from data import db

app = FastAPI()

@app.get("/")
def home():
    return {"message": "Welcome to FastAPI CRUD Example!"}

@app.get("/items/")
def read_items():
    return db

@app.get("/items/{item_id}")
def read_item(item_id: int):
    item = db.get(item_id)
    if item:
        return item
    raise HTTPException(status_code=404, detail="Item not found")

@app.post("/items/")
def create_item(item: Item):
    db[item.id] = item
    return {"message": "Item created successfully", "item": item}

@app.put("/items/{item_id}")
def update_item(item_id: int, item: Item):
    if item_id in db:
        db[item_id] = item
        return {"message": "Item updated", "item": item}
    raise HTTPException(status_code=404, detail="Item not found")

@app.delete("/items/{item_id}")
def delete_item(item_id: int):
    if item_id in db:
        del db[item_id]
        return {"message": "Item deleted"}
    raise HTTPException(status_code=404, detail="Item not found")
