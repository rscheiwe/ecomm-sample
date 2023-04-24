from datetime import datetime
from sqlalchemy import Boolean, ForeignKey, Column, Integer, String, DateTime
from sqlalchemy.orm import relationship
from sqlalchemy.sql import func
from project.database import Base


class User(Base):
    __tablename__ = 'users'

    id = Column(Integer, primary_key=True, autoincrement=True)
    main_id = Column(Integer, unique=True)
    name = Column(String, nullable=True)
    email = Column(String, nullable=True)
    password_hash = Column(String, nullable=True)
    password_plain = Column(String, nullable=True)
    superadmin = Column(Boolean, default=False)
    shop_name = Column(String, nullable=True)
    remember_token = Column(String, nullable=True, default=None)
    created_at = Column(DateTime)
    updated_at = Column(DateTime)
    card_brand = Column(String, nullable=True)
    card_last_four = Column(Integer)
    trial_ends_at = Column(DateTime)
    shop_domain = Column(String, nullable=True)
    is_enabled = Column(Boolean, default=True)
    billing_plan = Column(String, nullable=True)
    trial_starts_at = Column(DateTime)

    user_roles = relationship("UserRole", back_populates="user")
    products = relationship('Product', back_populates='admin_owner')

    def __init__(self,
                 main_id,
                 name,
                 email,
                 password_hash,
                 password_plain,
                 superadmin,
                 shop_name,
                 remember_token,
                 created_at,
                 updated_at,
                 card_brand,
                 card_last_four,
                 trial_ends_at,
                 shop_domain,
                 is_enabled,
                 billing_plan,
                 trial_starts_at
                 ):
        self.main_id = main_id
        self.name = name
        self.email = email
        self.password_hash = password_hash
        self.password_plain = password_plain
        self.superadmin = superadmin
        self.shop_name = shop_name
        self.remember_token = remember_token
        self.created_at = created_at
        self.updated_at = updated_at
        self.card_brand = card_brand
        self.card_last_four = card_last_four
        self.trial_ends_at = trial_ends_at
        self.shop_domain = shop_domain
        self.is_enabled = is_enabled
        self.billing_plan = billing_plan
        self.trial_starts_at = trial_starts_at

#
# class User(Base):
#     __tablename__ = 'users'
#
#     id = Column(Integer, primary_key=True, autoincrement=True)
#     username = Column(String, nullable=True)
#     email = Column(String, unique=True, index=True, nullable=False)
#     hashed_password = Column(String)
#     is_active = Column(Boolean, default=True, nullable=False)
#
#     user_roles = relationship("UserRole", back_populates="user")
#     properties = relationship('Property', back_populates='owner')
#
#     def __init__(self, username, email, hashed_password, is_active):
#         self.username = username
#         self.email = email
#         self.hashed_password = hashed_password
#         self.is_active = is_active


class Role(Base):
    __tablename__ = "roles"

    id = Column(Integer, primary_key=True, index=True, autoincrement=True)
    role_name = Column(String, index=True)
    created = Column(DateTime, default=func.now())

    user_roles = relationship("UserRole", back_populates="role")

    def __init__(self, role_name, created=None):
        self.role_name = role_name
        self.created_at = created if created is not None else datetime.now()


class UserRole(Base):
    __tablename__ = "userroles"

    id = Column(Integer, primary_key=True, index=True)
    user_id = Column(Integer, ForeignKey("users.id"))
    role_id = Column(Integer, ForeignKey("roles.id"))
    role_name = Column(String)

    user = relationship("User", back_populates="user_roles")
    role = relationship("Role", back_populates="user_roles")
