from pydantic import BaseModel


class InventoryBase(BaseModel):
    id: int


class InventoryCreate(InventoryBase):
    pass


class Inventory(InventoryBase):
    main_id: int
    product_id: int
    quantity: int
    color: str

    class Config:
        orm_mode = True


class InventoryProductResult(BaseModel):
    inventory_id: int
    product_name: str
    brand: str
    color: str
    description: str
    product_id: int
    quantity: int
    size: str
    sku: str
    style: str
    price_cents: str
    cost_cents: str

    class Config:
        orm_mode = True