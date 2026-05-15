from sqlalchemy import Column, Enum, Integer, String, Text

from src.db.connection import Base


class Contenidos(Base):
    __tablename__ = "contenidos"

    id = Column(Integer, primary_key=True)
    titulo = Column(String(255), nullable=False)
    tipo = Column(Enum("pelicula", "serie", name="tipo_contenido"), nullable=False)
    anio = Column(Integer)
    descripcion = Column(Text, nullable=True)
    duracion_min = Column(Integer)
    clasificacion_edad = Column(Enum('ATP', '+13', '+16', '+18', name='tipo_clasificacion'), nullable=False)
