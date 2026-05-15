from sqlalchemy import Column, Integer, String, Boolean, DateTime, ForeignKey
from sqlalchemy.sql import func

from src.db.connection import Base


class Perfiles(Base):
    __tablename__ = "perfiles"

    id = Column(Integer, primary_key=True)
    cuenta_id = Column(Integer, ForeignKey("cuentas.id"), nullable=False)
    nombre = Column(String(50), nullable=False)
    es_infantil = Column(Boolean, default=False)
    avatar = Column(String(255), nullable=True)
    bloqueado_hasta = Column(DateTime, nullable=True)
    intentos_fallidos_pin = Column(Integer, default=0)


