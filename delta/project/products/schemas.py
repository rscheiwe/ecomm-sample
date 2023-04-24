from typing import List, Optional, Union
from pydantic import BaseModel
from enum import Enum
from project.inventories.schemas import Inventory


class ProductBase(BaseModel):
    id: int


class ProductCreate(ProductBase):
    pass


class Product(ProductBase):
    id: int
    product_name: str
    style: Union[str, None] = None
    brand: Union[str, None] = None
    inventory: List[Inventory] = []
    admin_id: int

    class Config:
        orm_mode = True