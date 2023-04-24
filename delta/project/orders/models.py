from sqlalchemy import Boolean, Column, ForeignKey, DateTime, Integer, String, Float
from sqlalchemy.orm import relationship
from project.products.models import Product
from project.inventories.models import Inventory

from project.database import Base


class Order(Base):
    __tablename__ = 'orders'

    id = Column(Integer, primary_key=True, autoincrement=True)
    main_id = Column(Integer, unique=True)
    product_id = Column(Integer, ForeignKey(Product.main_id))
    inventory_id = Column(Integer, ForeignKey(Inventory.main_id))
    street_address = Column(String, nullable=True)
    apartment = Column(String, nullable=True)
    city = Column(String, nullable=True)
    state = Column(String, nullable=True)
    country_code = Column(String, nullable=True)
    zip = Column(Integer, nullable=True)
    phone_number = Column(Integer, nullable=True)
    email = Column(String, nullable=True)
    name = Column(String, nullable=True)
    order_status = Column(String, nullable=True)
    payment_ref = Column(String, nullable=True)
    transaction_id = Column(String, nullable=True)
    payment_amt_cents = Column(Integer, nullable=True)
    ship_charged_cents = Column(Float, nullable=True)
    ship_cost_cents = Column(Float, nullable=True)
    subtotal_cents = Column(Integer, nullable=True)
    total_cents = Column(Integer, nullable=True)
    shipper_name = Column(String, nullable=True)
    payment_date = Column(String, nullable=True)
    shipped_date = Column(String, nullable=True)
    tracking_number = Column(String, nullable=True)
    tax_total_cents = Column(Integer, nullable=True)
    created_at = Column(DateTime)
    updated_at = Column(DateTime)

    # product_owner = relationship('Product', back_populates='orders')
    # inventory_owner = relationship('Inventory', back_populates='orders')

    def __init__(self,
                 main_id,
                 product_id,
                 inventory_id,
                 street_address,
                 apartment,
                 city,
                 state,
                 country_code,
                 zip,
                 phone_number,
                 email,
                 name,
                 order_status,
                 payment_ref,
                 transaction_id,
                 payment_amt_cents,
                 ship_charged_cents,
                 ship_cost_cents,
                 subtotal_cents,
                 total_cents,
                 shipper_name,
                 payment_date,
                 shipped_date,
                 tracking_number,
                 tax_total_cents,
                 created_at,
                 updated_at,
                 ):
        self.main_id = main_id
        self.product_id = product_id
        self.inventory_id = inventory_id
        self.street_address = street_address
        self.apartment = apartment
        self.city = city
        self.state = state
        self.country_code = country_code
        self.zip = zip
        self.phone_number = phone_number
        self.email = email
        self.name = name
        self.order_status = order_status
        self.payment_ref = payment_ref
        self.transaction_id = transaction_id
        self.payment_amt_cents = payment_amt_cents
        self.ship_charged_cents = ship_charged_cents
        self.ship_cost_cents = ship_cost_cents
        self.subtotal_cents = subtotal_cents
        self.total_cents = total_cents
        self.shipper_name = shipper_name
        self.payment_date = payment_date
        self.shipped_date = shipped_date
        self.tracking_number = tracking_number
        self.tax_total_cents = tax_total_cents
        self.created_at = created_at
        self.updated_at = updated_at

#
#
# class Property(Base):
#     __tablename__ = 'properties'
#
#     id = Column(Integer, primary_key=True, autoincrement=True)
#     property_address = Column(String, unique=True, nullable=False)
#
#     owner_id = Column(Integer, ForeignKey('users.id'))
#
#     owner = relationship('User', back_populates='properties')
#
#     def __init__(self, property_address, owner_id):
#         self.property_address = property_address
#         self.owner_id = owner_id

