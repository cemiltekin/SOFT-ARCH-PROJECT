from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from fastapi.staticfiles import StaticFiles

import models
from database import Base, SessionLocal, engine
from routers import router

app = FastAPI(title="YummyFast Online Catering Service")

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"]
)

app.include_router(router)


def initialize_database() -> None:
    Base.metadata.create_all(bind=engine)

    db = SessionLocal()
    try:
        has_menus = db.query(models.Menu).first() is not None
        if has_menus:
            return

        dummy_menus = [
            models.Menu(
                name="Classic Business Lunch",
                description="Grilled chicken, rice, salad, dessert and soft drink.",
                price=18.50
            ),
            models.Menu(
                name="Vegetarian Catering Box",
                description="Vegetable pasta, seasonal salad, fruit cup and lemonade.",
                price=16.00
            ),
            models.Menu(
                name="Executive Buffet Menu",
                description="Beef sliders, wraps, appetizers, dessert tray and beverages.",
                price=29.90
            )
        ]
        db.add_all(dummy_menus)
        db.commit()
    finally:
        db.close()


@app.on_event("startup")
def on_startup() -> None:
    initialize_database()


app.mount("/", StaticFiles(directory="static", html=True), name="static")
