from sqlalchemy import Column, Integer, ForeignKey

from src.db.connection import Base


class Temporadas(Base):
    __tablename__ = "temporadas"

    id = Column(Integer, primary_key=True)
    contenido_id = Column(Integer, ForeignKey("contenidos.id"), nullable=False)
    numero = Column(Integer, nullable=False)
    anio = Column(Integer)
