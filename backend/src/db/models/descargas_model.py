from sqlalchemy import Column, Integer, DateTime, ForeignKey, Boolean
from sqlalchemy.sql import func

from src.db.connection import Base


class Descargas(Base):
    __tablename__ = "descargas"

    id = Column(Integer, primary_key=True)
    perfil_id = Column(Integer, ForeignKey("perfiles.id"), nullable=False)
    contenido_id = Column(Integer, ForeignKey("contenidos.id"), nullable=False)
    episodio_id = Column(Integer, ForeignKey("episodios.id"), nullable=True)
    fecha_descarga = Column(DateTime, server_default=func.now())
    vencimiento = Column(DateTime)
    activa = Column(Boolean, default=True)
