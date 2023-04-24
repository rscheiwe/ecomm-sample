
from typing import List
from fastapi import Depends, HTTPException
from sqlalchemy.orm import Session
from project.database import get_db_session

from project.inventories import crud, schemas, models
from project.users import crud as user_crud
from project.users import schemas as user_schemas
from project.security import get_current_user, RoleChecker
from . import inventory_router


def format_price(price_in_cents):
    dollars = price_in_cents / 100
    formatted_dollars = f"${dollars:.2f}"
    return formatted_dollars


@inventory_router.get(
    "/current-user-inventory",
    # response_model=List[schemas.Inventory]
    response_model=List[schemas.InventoryProductResult]
)
def get_user_inventory(
        current_user= Depends(get_current_user),
        db: Session = Depends(get_db_session)
):
    """
    - Display the Product Name, sku, quantity, color, size, price and cost
    - Show the total count of inventory items in the system for the user
    - Allow the user to filter the list for a specific product id or sku
    """
    db_user = user_crud.get_user_by_email(db, email=current_user.email)
    db_user_inventory = crud.get_user_inventory_by_user_product(db, user_id=current_user.main_id)

    keys_to_extract = [
        'product_name',
        'brand',
        'color',
        'description',
        'product_id',
        'quantity',
        'size',
        'sku',
        'style',
        'price_cents',
        'cost_cents',
    ]
    result = []

    for inv, pro in db_user_inventory:
        combined_dict = {**vars(inv), **vars(pro)}
        filtered_dict = {k: v for k, v in combined_dict.items() if k in keys_to_extract}
        filtered_dict['inventory_id'] = vars(inv)['main_id']
        filtered_dict['price_cents'] = format_price(filtered_dict['price_cents'])
        filtered_dict['cost_cents'] = format_price(filtered_dict['cost_cents'])
        result.append(filtered_dict)

    if not db_user:
        raise HTTPException(status_code=404, detail="User not found.")
    return result
