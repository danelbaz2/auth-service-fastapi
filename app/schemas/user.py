#Schemas for Swagger UI
from __future__ import annotations
from pydantic import BaseModel, EmailStr, Field, ConfigDict
from enum import StrEnum
from typing import List, Optional
from datetime import datetime

# --- INPUT ---------------------------

class UserStatus(StrEnum):
    active = 'active'
    pending = 'pending'
    disabled = 'disabled'

class UserBase(BaseModel):
    email: EmailStr = Field(..., description="User email (validated)")
    model_config = ConfigDict(from_attributes=True)

class UserCreate(UserBase):
    email: EmailStr
    password: str = Field(..., min_length=8, max_length=128)

class UserLogin(BaseModel):
    email: EmailStr
    password: str = Field(..., min_length=8, max_length=128)

class UserUpdate(BaseModel):
    status: Optional[UserStatus] = None

    model_config = ConfigDict(from_attributes=True)

# --- OUTPUT ---------------------------

class RoleOut(BaseModel):
    id: int
    name: str

    model_config = ConfigDict(from_attributes=True)

class UserResponse(UserBase):
    user_id: int
    email: EmailStr
    role: int
    status: str
    created_at: datetime
    model_config = ConfigDict(from_attributes=True)