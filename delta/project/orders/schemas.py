from typing import List, Optional
from pydantic import BaseModel
from enum import Enum


class OrderBase(BaseModel):
    id: int


class OrderCreate(OrderBase):
    pass


class Order(OrderBase):
    id: int
    main_id: str
    product_id: int
    inventory_id: int
    street_address: str

    class Config:
        orm_mode = True
