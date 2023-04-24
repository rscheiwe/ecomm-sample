from typing import List
from project.users import models
from project.users import schemas
from sqlalchemy.orm import Session
from project.products.models import Product
from project.security import get_password_hash


def get_user(db: Session, user_id: int):
    return db.query(models.User).filter(models.User.id == user_id).first()


def get_user_by_email(db: Session, email: str):
    test = db.query(models.User).filter(models.User.email == email).first()
    print(test)
    return db.query(models.User).filter(models.User.email == email).first()


def get_users(db: Session, skip: int = 0, limit: int = 100):
    return db.query(models.User).offset(skip).limit(limit).all()


def get_user_products(db: Session, admin_id: int):
    return db.query(Product).filter(Product.admin_id == admin_id).all()


def get_roles_by_username(db: Session, username: str):
    user = db.query(models.User).filter(models.User.username == username).first()
    # return user.user_roles
    return user.user_roles[0].role_name


def get_role_names(db: Session, roles: List[models.UserRole]):
    names = list()
    for role in roles:
        role_item = db.query(models.Role).filter(models.Role.id == role.id).first()
        names.append(role_item.role_name)

    return names




