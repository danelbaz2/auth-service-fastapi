from datetime import datetime
from sqlalchemy import Column, ForeignKey, Integer, String, Text
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import DateTime
from sqlalchemy import Enum
from sqlalchemy import func


Base = declarative_base()

class User(Base):
    __tablename__ = 'users'
    id = Column(Integer, primary_key=True)
    email = Column(String, unique=True, nullable=False)
    password_hash = Column(String, nullable=False)
    status = Column(Enum('active', 'pending', 'disabled', name='user_status'), server_default='active', nullable=False)
    created_at = Column(DateTime, server_default=func.now(), nullable=False)

class Role(Base):
    __tablename__ = 'roles'
    id = Column(Integer, primary_key=True)
    name = Column(String, unique=True, nullable=False)

class UserRole(Base):
    __tablename__ = 'user_roles'
    user_id = Column(Integer, ForeignKey('users.id', ondelete='CASCADE'), primary_key=True)
    role_id = Column(Integer, ForeignKey('roles.id', ondelete='CASCADE'), primary_key=True)

class Document(Base):
    __tablename__ = 'documents'
    id = Column(Integer, primary_key=True)
    title = Column(String(255), nullable=False)
    content = Column(Text, nullable=False)
    created_by = Column(Integer, ForeignKey('users.id', ondelete='CASCADE'), nullable=False)
    created_at = Column(DateTime, server_default=func.now(), nullable=False)