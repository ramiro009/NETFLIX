from sqlalchemy import Column, Integer, Boolean, DateTime, ForeignKey
from sqlalchemy.sql import func

from src.db.connection import Base


class Vistas(Base):
    __tablename__ = "vistas"

    id = Column(Integer, primary_key=True)
    perfil_id = Column(Integer, ForeignKey("perfiles.id"), nullable=False)
    episodio_id = Column(Integer, ForeignKey("episodios.id"), nullable=False)
    fecha = Column(DateTime, server_default=func.now())
    segundo_actual = Column(Integer, default=0)
    terminado = Column(Boolean, default=False)
