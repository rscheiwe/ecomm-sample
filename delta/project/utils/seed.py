import os
import csv
from datetime import datetime
import pathlib
from contextlib import contextmanager
from sqlalchemy import Boolean, Column, ForeignKey, Integer, String, DateTime, Float
from sqlalchemy.orm import relationship, declarative_base
from sqlalchemy.sql import func
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

_inc = 1

BASE_DIR: pathlib.Path = pathlib.Path(__file__).parent.parent.parent
DATA_DIR: pathlib.Path = f"{BASE_DIR}/jupyter/data"

def _get_str_inc():
    global _inc
    s = str(_inc)
    _inc = _inc + 1
    return s


def _reset_inc():
    global _inc
    _inc = 1


DATABASE_URL: str = os.environ.get(
    "DATABASE_URL",
    f"sqlite:///./sql_app.db"
)

DATABASE_CONNECT_DICT: dict = {"check_same_thread": False}

engine = create_engine(
    DATABASE_URL,
    connect_args=DATABASE_CONNECT_DICT,
    pool_recycle=1800,
     echo=True
)

SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

Base = declarative_base()


def get_db_session():
    session = SessionLocal()
    try:
        yield session
    finally:
        session.close()


db_context = contextmanager(get_db_session)


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

    def __init__(self, user_id, role_id, role_name):
        self.user_id = user_id
        self.role_id = role_id
        self.role_name = role_name

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


session = SessionLocal()


with db_context() as session:
#
    session.query(User).delete()
    session.query(Order).delete()
    session.query(Role).delete()
    session.query(UserRole).delete()
    session.query(Product).delete()
    session.query(Inventory).delete()
#
    role_admin = Role(
        role_name="ADMIN",
    )
    role_user = Role(
        role_name="USER"
    )

    session.add_all([role_admin, role_user])
    _reset_inc()

    with open(f"{DATA_DIR}/users.csv", 'r') as csv_file:
        reader = csv.DictReader(csv_file)

        # loop through each row in the CSV file
        for row in reader:
            # create a new User object with the data from the row
            user = User(
                main_id=int(row['id']),
                name=row['name'],
                email=row['email'],
                password_hash=row['password_hash'],
                password_plain=row['password_plain'],
                superadmin=bool(row['superadmin']),
                shop_name=row['shop_name'],
                remember_token=row['remember_token'],
                created_at=datetime.strptime(row['created_at'], '%Y-%m-%d %H:%M:%S'),
                updated_at=datetime.strptime(row['updated_at'], '%Y-%m-%d %H:%M:%S'),
                card_brand=row['card_brand'],
                card_last_four=int(row['card_last_four']),
                trial_ends_at=datetime.strptime(row['trial_ends_at'], '%Y-%m-%d %H:%M:%S'),
                shop_domain=row['shop_domain'],
                is_enabled=bool(row['is_enabled']),
                billing_plan=row['billing_plan'],
                trial_starts_at=datetime.strptime(row['trial_starts_at'], '%Y-%m-%d %H:%M:%S')
            )
            session.add(user)
            session.commit()

    with open(f"{DATA_DIR}/products.csv", 'r') as csv_file:
        reader = csv.DictReader(csv_file)

        # loop through each row in the CSV file
        for row in reader:
            # create a new User object with the data from the row
            product = Product(
                main_id=int(row['id']),
                product_name=row['product_name'],
                description=row['description'],
                style=row['style'],
                brand=row['brand'],
                created_at=datetime.strptime(row['created_at'], '%Y-%m-%d %H:%M:%S'),
                updated_at=datetime.strptime(row['updated_at'], '%Y-%m-%d %H:%M:%S'),
                url=row['url'],
                product_type=row['product_type'],
                shipping_price=int(row['shipping_price']),
                note=row['note'],
                admin_id=int(row['admin_id'])
            )
            session.add(product)
            session.commit()

    with open(f"{DATA_DIR}/inventory.csv", 'r') as csv_file:
        reader = csv.DictReader(csv_file)

        # loop through each row in the CSV file
        for row in reader:
            # create a new User object with the data from the row
            inventory = Inventory(
                main_id=row['id'],
                product_id=row['product_id'],
                quantity=row['quantity'],
                color=row['color'],
                size=row['size'],
                weight=row['weight'],
                price_cents=row['price_cents'],
                sale_price_cents=row['sale_price_cents'],
                cost_cents=row['cost_cents'],
                sku=row['sku'],
                length=row['length'],
                width=row['width'],
                height=row['height'],
                note=row['note'],
            )
            session.add(inventory)
            session.commit()

    with open(f"{DATA_DIR}/orders.csv", 'r') as csv_file:
        reader = csv.DictReader(csv_file)

        # loop through each row in the CSV file
        for row in reader:
            for key, value in row.items():
                if value == 'NULL':
                    row[key] = None
            # Convert date strings to datetime objects
            row['created_at'] = datetime.strptime(row['created_at'], '%Y-%m-%d %H:%M:%S')
            row['updated_at'] = datetime.strptime(row['updated_at'], '%Y-%m-%d %H:%M:%S')

            # Create an instance of the Order class using the row data
            order = Order(
                main_id=row['id'],
                product_id=row['product_id'],
                inventory_id=row['inventory_id'],
                street_address=row['street_address'],
                apartment=row['apartment'],
                city=row['city'],
                state=row['state'],
                country_code=row['country_code'],
                zip=row['zip'],
                phone_number=row['phone_number'],
                email=row['email'],
                name=row['name'],
                order_status=row['order_status'],
                payment_ref=row['payment_ref'],
                transaction_id=row['transaction_id'],
                payment_amt_cents=row['payment_amt_cents'],
                ship_charged_cents=row['ship_charged_cents'],
                ship_cost_cents=row['ship_cost_cents'],
                subtotal_cents=row['subtotal_cents'],
                total_cents=row['total_cents'],
                shipper_name=row['shipper_name'],
                payment_date=row['payment_date'],
                shipped_date=row['shipped_date'],
                tracking_number=row['tracking_number'],
                tax_total_cents=row['tax_total_cents'],
                created_at=row['created_at'],
                updated_at=row['updated_at'],
            )
            session.add(order)
            session.commit()


if __name__ == '__main__':
    print(DATA_DIR)