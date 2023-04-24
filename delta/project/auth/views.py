from fastapi import Depends, HTTPException, status
from datetime import timedelta
from project.security import create_access_token, authenticate_user, ACCESS_TOKEN_EXPIRE_MINUTES
from fastapi.security import OAuth2PasswordRequestForm
from . import auth_router
from pydantic import BaseModel
from project.users.crud import get_user_products
from sqlalchemy.orm import Session
from project.database import get_db_session


class Token(BaseModel):
    access_token: str
    token_type: str
    data: dict


@auth_router.post("/token", response_model=Token)
async def login_for_access_token(
        form_data: OAuth2PasswordRequestForm = Depends(),
        db: Session = Depends(get_db_session)
):
    user = authenticate_user(form_data.username, form_data.password)
    if not user:
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="Incorrect username or password",
            headers={"WWW-Authenticate": "Bearer"},
        )
    access_token_expires = timedelta(minutes=ACCESS_TOKEN_EXPIRE_MINUTES)
    access_token = create_access_token(
        data={"sub": user.__dict__["email"]}, expires_delta=access_token_expires
    )
    user_products = get_user_products(db, user.__dict__["main_id"])
    user.__dict__["products"] = user_products
    print(user_products)
    return {
        "access_token": access_token,
        "token_type": "bearer",
        "data": {
            "user": user,
        }
    }
