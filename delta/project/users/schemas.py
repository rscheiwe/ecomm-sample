from typing import List, Union
from pydantic import BaseModel
import datetime
from project.products.schemas import Product


class UserRoleBase(BaseModel):
    id: int


class UserRole(UserRoleBase):
    role_id: int
    role_name: str

    class Config:
        orm_mode = True


class RoleBase(BaseModel):
    role_name: str


class UserBase(BaseModel):
    email: str
    name: str
    shop_name: str
    superadmin: bool
    created_at: datetime.datetime
    card_brand: str
    card_last_four: int
    billing_plan: str
    trial_starts_at: datetime.datetime
    trial_ends_at: datetime.datetime
    user_roles: List[UserRole] = []
    products: List[Product] = []

    class Config:
        orm_mode = True


class UserToken(BaseModel):
    email: str
    token: str


class Token(BaseModel):
    access_token: str
    token_type: str
    data: dict


class TokenData(BaseModel):
    email: Union[str, None] = None
