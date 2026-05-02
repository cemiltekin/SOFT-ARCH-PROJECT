from sqlalchemy.orm import Session

import repository
import schemas


def get_available_menus(db: Session):
    menus = repository.get_all_menus(db)
    return [menu for menu in menus if menu.is_available]


def place_order(db: Session, order_data: schemas.OrderCreate):
    menu = repository.get_menu_by_id(db, order_data.menu_id)
    if menu is None:
        raise ValueError("Menu item was not found.")
    if not menu.is_available:
        raise ValueError("Menu item is not available.")

    # Payment is mocked for Phase 1; a successful payment creates the order.
    return repository.create_order(db, order_data, menu)
