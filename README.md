# YummyFast - Online Catering Service

Phase 1 implementation using Layered Architecture.

## Layers

- Presentation Layer: `static/index.html`
- Control Layer: `routers.py`
- Domain Layer: `models.py`, `schemas.py`, `services.py`
- Resource Layer: `database.py`, `repository.py`, SQLite database
- Documentation: `SAD_Phase1.md`

## Run

```powershell
python -m venv .venv
.\.venv\Scripts\Activate.ps1
pip install -r requirements.txt
uvicorn main:app --reload
```

Then open `http://localhost:8000`.

## API

- `GET /menus`
- `POST /orders`
