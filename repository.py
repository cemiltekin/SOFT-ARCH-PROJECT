from sqlalchemy.orm import Session

import models
import schemas


def get_all_menus(db: Session) -> list[models.Menu]:
    return db.query(models.Menu).order_by(models.Menu.id).all()


def get_menu_by_id(db: Session, menu_id: int) -> models.Menu | None:
    return db.query(models.Menu).filter(models.Menu.id == menu_id).first()


def create_order(db: Session, order_data: schemas.OrderCreate, menu: models.Menu) -> models.Order:
    order = models.Order(
        customer_name=order_data.customer_name,
        address=order_data.address,
        menu_id=menu.id,
        total_amount=menu.price,
        status="PAID"
    )
    db.add(order)
    db.commit()
    db.refresh(order)
    return order
