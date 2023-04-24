from fastapi import APIRouter


users_router = APIRouter(
    prefix="/delta-users",
    tags=["Users"],
)

from . import views, models # noqa
