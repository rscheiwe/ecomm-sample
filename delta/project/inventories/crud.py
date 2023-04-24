from project.inventories.models import Inventory
from project.products.models import Product
from project.users.models import User

from sqlalchemy.orm import Session


def get_user_inventory_by_user_product(db: Session, user_id: int):
    return (
        db.query(Inventory, Product)
        .join(Product)
        .join(User)
        .filter(User.main_id == user_id)
        .filter(Product.admin_id == User.main_id)
        .filter(Inventory.product_id == Product.main_id)
    ).all()
