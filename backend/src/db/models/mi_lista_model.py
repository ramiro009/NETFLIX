from sqlalchemy import Column, Integer, DateTime, ForeignKey, UniqueConstraint
from sqlalchemy.sql import func

from src.db.connection import Base


class MiLista(Base):
    __tablename__ = "mi_lista"

    perfil_id = Column(Integer, ForeignKey("perfiles.id"), nullable=False)
    contenido_id = Column(Integer, ForeignKey("contenidos.id"), nullable=False)
    fecha_agregada = Column(DateTime, server_default=func.now())