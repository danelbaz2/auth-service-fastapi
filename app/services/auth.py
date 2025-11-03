# app/services/auth.py
from sqlalchemy.orm import Session
from app.models.user import User
from app.services.security import hash_password
from app.schemas.user import UserCreate

def create_user(db: Session, user_in: UserCreate):
    existing_user = db.query(User).filter(User.email == user_in.email).first()
    if existing_user:
        raise ValueError("Email already registered")

    new_user = User(
        email=user_in.email,
        password_hash=hash_password(user_in.password),
        role=5,  # guest by default
    )
    db.add(new_user)
    db.commit()
    db.refresh(new_user)
    return new_user
