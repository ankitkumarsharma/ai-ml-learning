# FastAPI CRUD
1. pip install fastapi uvicorn sqlalchemy
2. uvicorn main:app --reload
3. http://localhost:8000/docs
4. 
```python
from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
from typing import List

app = FastAPI()

# Pydantic model for data validation
class Item(BaseModel):
    id: int
    name: str
    price: float

# In-memory "database"
items = []

# Create (POST)
@app.post("/items/", response_model=Item)
def create_item(item: Item):
    items.append(item)
    return item

# Read all (GET)
@app.get("/items/", response_model=List[Item])
def read_items():
    return items

# Read one by ID (GET)
@app.get("/items/{item_id}", response_model=Item)
def read_item(item_id: int):
    for item in items:
        if item.id == item_id:
            return item
    raise HTTPException(status_code=404, detail="Item not found")

# Update (PUT)
@app.put("/items/{item_id}", response_model=Item)
def update_item(item_id: int, updated_item: Item):
    for index, item in enumerate(items):
        if item.id == item_id:
            items[index] = updated_item
            return updated_item
    raise HTTPException(status_code=404, detail="Item not found")

# Delete (DELETE)
@app.delete("/items/{item_id}")
def delete_item(item_id: int):
    for index, item in enumerate(items):
        if item.id == item_id:
            del items[index]
            return {"message": "Item deleted"}
    raise HTTPException(status_code=404, detail="Item not found")
```