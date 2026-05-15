from sqlalchemy import Column, Enum, Integer, String, Text

from src.db.connection import Base


class ContenidoGeneros(Base):
    __tablename__ = "contenidoGeneros"

    contenido_id = Column(Integer, primary_key=True)
    genero_id = Column(Integer, nullable=False)