from sqlalchemy import Column, Integer, String

from src.db.connection import Base


class Idiomas(Base):
    __tablename__ = "idiomas"

    id = Column(Integer, primary_key=True)
    nombre = Column(String(50), nullable=False, unique=True)
    codigo = Column(String(2), nullable=False, unique=True)
