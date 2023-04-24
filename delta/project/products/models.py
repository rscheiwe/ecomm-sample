from sqlalchemy import Boolean, Column, ForeignKey, DateTime, Integer, String, Float
from sqlalchemy.orm import relationship

from project.database import Base


class Product(Base):
    __tablename__ = 'products'

    id = Column(Integer, primary_key=True, autoincrement=True)
    main_id = Column(Integer)
    product_name = Column(String, nullable=True)
    description = Column(String, nullable=True)
    style = Column(String, nullable=True)
    brand = Column(String, nullable=True)
    created_at = Column(String, nullable=True)
    updated_at = Column(String, nullable=True)
    url = Column(String, nullable=True)
    product_type = Column(String, nullable=True)
    shipping_price = Column(Integer, nullable=True)
    note = Column(String, nullable=True)
    admin_id = Column(Integer, ForeignKey('users.main_id'))

    admin_owner = relationship('User', back_populates='products')
    inventories = relationship('Inventory', back_populates='product_owner')


    def __init__(self,
                 main_id,
                 product_name,
                 description,
                 style,
                 brand,
                 created_at,
                 updated_at,
                 url,
                 product_type,
                 shipping_price,
                 note,
                 admin_id,
                 ):
        self.main_id = main_id
        self.product_name = product_name
        self.description = description
        self.style = style
        self.brand = brand
        self.created_at = created_at
        self.updated_at = updated_at
        self.url = url
        self.product_type = product_type
        self.shipping_price = shipping_price
        self.note = note
        self.admin_id = admin_id