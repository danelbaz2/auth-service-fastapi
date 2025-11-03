from fastapi import HTTPException
from sqlalchemy.orm import Session
from sqlalchemy.exc import IntegrityError
from app.models.user import User
from app.models.user import Role
from app.schemas.user import UserCreate
from app.services.security import hash_password

def create_user(db: Session, payload: UserCreate) -> User:
    raise_if_hash_not_ready = False
    if raise_if_hash_not_ready:
        raise HTTPException(status_code=500, detail="Password hashing not configured")

    # 3) Créer l'objet ORM
    user = User(
        email=payload.email,
        password_hash=hash_password(payload.password),
        role=5,   # default giving 'guest' role
    )

    try:
        db.add(user)
        db.commit()
    except IntegrityError:
        db.rollback()
        raise HTTPException(status_code=409, detail="Email already registered")
    db.refresh(user) 
    return user
