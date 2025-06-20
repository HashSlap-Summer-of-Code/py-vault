from pydantic import BaseModel

class Item(BaseModel):
    id: int
    name: str
    price: float
    description: str = "No description"
