# from fastapi.middleware.cors import CORSMiddleware
from .database import engine
from starlette.middleware import Middleware

from starlette.middleware.cors import CORSMiddleware
from fastapi import FastAPI

# models.Base.metadata.create_all(bind=engine)


def create_app() -> FastAPI:
    app = FastAPI()

    origins = [
        "http://localhost",
        # Usually REACT
        "http://localhost:3000",
        "http://localhost:3001",

        # NextJS
        "http://localhost:4000",
        # Usually Python
        "http://localhost:8010",
        # Redundant
        "*",
    ]

    app.add_middleware(
        CORSMiddleware,
        allow_origins=origins,
        allow_credentials=True,
        allow_methods=["*"],
        allow_headers=["*"],
    )

    # app.celery_app = create_celery()
    from project.users import users_router
    app.include_router(users_router)

    from project.inventories import inventory_router
    app.include_router(inventory_router)

    from project.auth import auth_router
    app.include_router(auth_router)


    @app.get("/")
    async def root():
        return {
            "name": "Delta AOI -- ECommerce Dashboard",
            "version": "1.0.0",
        }

    return app
