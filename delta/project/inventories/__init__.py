from fastapi import APIRouter


inventory_router = APIRouter(
    prefix="/delta-inventory",
    tags=["Inventory"],
)

from . import views, models # noqa