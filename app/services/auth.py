from fastapi import HTTPException
from sqlalchemy import func
from sqlalchemy.orm import Session
from sqlalchemy.exc import IntegrityError

from app.models.user import User
from app.schemas.user import UserCreate

def create_user(db: Session, payload: UserCreate) -> User:
    raise_if_hash_not_ready = False
    if raise_if_hash_not_ready:
        raise HTTPException(status_code=500, detail="Password hashing not configured")

    # 3) Créer l'objet ORM
    user = User(
        email=payload.email,
        password_hash="REPLACE_WITH_REAL_HASH",  # replace via hash_password()
        status=payload.status.value
    )

    # 4) Persister

    try:
        db.add(user)
        db.commit()
    except IntegrityError:
        raise HTTPException(400, "Email already registered")
    db.refresh(user)
    return user
