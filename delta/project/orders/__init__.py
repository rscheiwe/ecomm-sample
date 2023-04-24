from fastapi import APIRouter


orders_router = APIRouter(
    prefix="/delta-orders",
    tags=["Delta Orders"],
)

from . import views, models # noqa