from sqlalchemy import Column, Integer, String, Boolean, DateTime
from sqlalchemy.sql import func

from src.db.connection import Base


class User(Base):
    __tablename__ = "users"

    id = Column(Integer, primary_key=True)
    email = Column(String, unique=True, nullable=False)
    plan = Column(String, nullable=False)
    pin = Column(String, nullable=False)
    fecha_alta = Column(DateTime, server_default=func.now())