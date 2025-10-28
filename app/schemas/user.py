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
    status: UserStatus = Field(default=UserStatus.active, description="User status (enum)")

    model_config = ConfigDict(from_attributes=True)

class UserCreate(UserBase):
    password: str = Field(..., min_length=8, max_length=128, description="Password before hashing (8 chars minimum)")

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

class UserOut(UserBase):
    id: int
    created_at: datetime
    roles: Optional[List[RoleOut]] = None