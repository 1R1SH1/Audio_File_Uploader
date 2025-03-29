from sqlalchemy import Column, Integer, String, Boolean, DateTime, text
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()

class User(Base):
    __tablename__ = "users"

    id = Column(Integer, primary_key=True, index=True)
    username = Column(String(50), unique=True, nullable=False)
    email = Column(String(120), unique=True, nullable=False)
    is_active = Column(Boolean, default=True)
    created_at = Column(DateTime, server_default=text("now()"))
    updated_at = Column(DateTime, server_default=text("now()"))
    password = Column(String)  # Use proper hashing in production
    yandex_token = Column(String)