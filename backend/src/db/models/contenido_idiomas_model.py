from sqlalchemy import Column, Integer, String, ForeignKey, Enum

from src.db.connection import Base


class ContenidoIdiomas(Base):
    __tablename__ = "contenido_idiomas"

    id = Column(Integer, primary_key=True)
    contenido_id = Column(Integer, ForeignKey("contenidos.id"), nullable=False)
    idioma_id = Column(Integer, ForeignKey("idiomas.id"), nullable=False)
    tipo = Column(Enum('audio', 'subtitulo', name='tipo_audio_sub'), nullable=False)
