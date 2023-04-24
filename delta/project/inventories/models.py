from sqlalchemy import Boolean, Column, ForeignKey, DateTime, Integer, String, Float
from sqlalchemy.orm import relationship

from project.database import Base


class Inventory(Base):
    __tablename__ = 'inventories'

    id = Column(Integer, primary_key=True, autoincrement=True)
    main_id = Column(Integer)
    product_id = Column(Integer, ForeignKey('products.main_id'))
    quantity = Column(Integer, nullable=True)
    color = Column(String, nullable=True)
    size = Column(String, nullable=True)
    weight = Column(Integer, nullable=True)
    price_cents = Column(Integer, nullable=True)
    sale_price_cents = Column(Integer, nullable=True)
    cost_cents = Column(Integer, nullable=True)
    sku = Column(String, nullable=True)
    length = Column(Integer, nullable=True)
    width = Column(Integer, nullable=True)
    height = Column(Integer, nullable=True)
    note = Column(String, nullable=True)

    product_owner = relationship('Product', back_populates='inventories')

    def __init__(self,
                 main_id,
                 product_id,
                 quantity,
                 color,
                 size,
                 weight,
                 price_cents,
                 sale_price_cents,
                 cost_cents,
                 sku,
                 length,
                 width,
                 height,
                 note,
                 ):
        self.main_id = main_id
        self.product_id = product_id
        self.quantity = quantity
        self.color = color
        self.size = size
        self.weight = weight
        self.price_cents = price_cents
        self.sale_price_cents = sale_price_cents
        self.cost_cents = cost_cents
        self.sku = sku
        self.length = length
        self.width = width
        self.height = height
        self.note = note