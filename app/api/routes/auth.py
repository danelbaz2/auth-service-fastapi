# app/api/routes/auth.py
from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy.orm import Session
from app.schemas.user import UserCreate, UserResponse
from app.services.auth import create_user
from app.dependencies import get_db

description=(
        "Creates a new user in the system.\n\n"
        "The user receives the default **guest role (role_id=5)** and an initial status of **active**. "
        "Returns the created user's public data (excluding password)."
    )
router = APIRouter(tags=["POST"])

@router.post("/auth/register",response_model=UserResponse,status_code=status.HTTP_201_CREATED,summary="Register a new user",description=description)
def register_user(payload: UserCreate, db: Session = Depends(get_db)):
    try:
        user = create_user(db, payload)
        return user
    except ValueError as e:
        raise HTTPException(status_code=status.HTTP_409_CONFLICT, detail=str(e))
