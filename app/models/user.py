from sqlalchemy import Column, ForeignKey, Integer, String, Text, text
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.dialects.postgresql import ENUM as PGEnum
from sqlalchemy import DateTime
from sqlalchemy import func
from enum import Enum


Base = declarative_base()

class UserStatus(str, Enum):
    active = "active"
    pending = "pending"
    disabled = "disabled"

class User(Base):
    __tablename__ = 'users'
    user_id = Column(Integer, primary_key=True, index=True)
    email = Column(String, unique=True, nullable=False)
    password_hash = Column(String, nullable=False)
    status = Column(PGEnum(UserStatus, name="user_status"), server_default="active", nullable=False)
    created_at = Column(DateTime, server_default=func.now(), nullable=False)
    role = Column(Integer, ForeignKey("roles.role_id"), server_default="5", nullable=False)
class Role(Base):
    __tablename__ = 'roles'
    role_id = Column(Integer, primary_key=True, index=True)
    name = Column(String, unique=True, nullable=False)

class Document(Base):
    __tablename__ = 'documents'
    document_id = Column(Integer, primary_key=True)
    title = Column(String(255), nullable=False)
    content = Column(Text, nullable=False)
    created_by = Column(Integer, ForeignKey('users.user_id', ondelete='CASCADE'), nullable=False)
    created_at = Column(DateTime, server_default=func.now(), nullable=False)