from fastapi import FastAPI, APIRouter, Depends, HTTPException, status
from sqlalchemy.orm import Session
<<<<<<< HEAD
=======
import asyncio, httpx, threading
>>>>>>> 255326d (Final)

from . import models, schemas, auth
from .database import Base, engine, get_db

# Create database tables on startup
Base.metadata.create_all(bind=engine)

# Initialize FastAPI app and router
app = FastAPI()
router = APIRouter(prefix="/user", tags=["user"])

<<<<<<< HEAD
=======
# ──────────────────────── ANALYTICS HELPER ───────────────────────
def _log_event_async(service: str, event_type: str, metadata: dict) -> None:
    """
    Non-blocking fire-and-forget analytics call.
    Thread-safe fallback if not in an active event loop.
    """
    async def _send() -> None:
        try:
            async with httpx.AsyncClient(verify=False, timeout=3) as c:
                await c.post(
                    "http://analytics-service:80/analytics/",
                    json={
                        "service": service,
                        "event_type": event_type,
                        "metadata": metadata,
                    },
                )
        except Exception as exc:
            print(f"[analytics] failed: {exc}")

    try:
        loop = asyncio.get_running_loop()
        loop.create_task(_send())
    except RuntimeError:
        # We're in a threadpool (no running loop) — safely launch with threading
        threading.Thread(target=lambda: asyncio.run(_send())).start()


# ──────────────────────────── ROUTES ─────────────────────────────
>>>>>>> 255326d (Final)

@router.post("/register", status_code=status.HTTP_201_CREATED)
def register(user: schemas.UserCreate, db: Session = Depends(get_db)):
    """Register a new user account."""
    if db.query(models.User).filter(models.User.email == user.email).first():
        raise HTTPException(status_code=400, detail="Email already registered")

    db_user = models.User(
        email=user.email,
        hashed_password=auth.hash_password(user.password),
    )
    db.add(db_user)
    db.commit()
    db.refresh(db_user)
<<<<<<< HEAD
=======

    _log_event_async(
        service="user-service",
        event_type="user_registered",
        metadata={"email": db_user.email},
    )

>>>>>>> 255326d (Final)
    return {"email": db_user.email}


@router.post("/login")
def login(user: schemas.UserCreate, db: Session = Depends(get_db)):
    """Authenticate a user with email & password (no JWT returned)."""
    db_user = db.query(models.User).filter(models.User.email == user.email).first()
    if not db_user or not auth.verify_password(
        user.password, db_user.hashed_password
    ):
        raise HTTPException(status_code=401, detail="Invalid credentials")

<<<<<<< HEAD
    return {"message": "Login successful"}


# Health endpoint
=======
    _log_event_async(
        service="user-service",
        event_type="user_login",
        metadata={"email": db_user.email},
    )

    return {"message": "Login successful"}


>>>>>>> 255326d (Final)
@router.get("/health", tags=["internal"])
def health():
    return {"status": "ok"}


# Register router with FastAPI app
app.include_router(router)

