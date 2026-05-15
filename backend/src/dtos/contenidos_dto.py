from datetime import datetime
from pydantic import BaseModel

class CreateContenidoDTO(BaseModel):
    titulo: str
    tipo: str
    clasificacion_edad: str


class ContenidoResponseDTO(BaseModel):
    id: int
    titulo: str
    tipo: int
    anio: int
    descripcion: str
    duracion_min: int
    clasificacio_edad: str


    model_config = {"from_attributes": True}
