from sqlalchemy import Column, Integer, DateTime, ForeignKey
from sqlalchemy.sql import func

from src.db.connection import Base


class Calificaciones(Base):
    __tablename__ = "calificaciones"

    id = Column(Integer, primary_key=True)
    perfil_id = Column(Integer, ForeignKey("perfiles.id"), nullable=False)
    contenido_id = Column(Integer, ForeignKey("contenidos.id"), nullable=False)
    puntaje = Column(Integer, nullable=False)
    fecha = Column(DateTime, server_default=func.now())
