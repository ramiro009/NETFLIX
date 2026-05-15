from sqlalchemy import Column, Integer, String, ForeignKey, UniqueConstraint

from src.db.connection import Base


class Episodios(Base):
    __tablename__ = "episodios"

    id = Column(Integer, primary_key=True)
    temporada_id = Column(Integer, ForeignKey("temporadas.id"), nullable=False)
    numero = Column(Integer, nullable=False)
    titulo = Column(String(255), nullable=False)
    duracion_min = Column(Integer, nullable=False)
