from datetime import datetime
from pydantic import BaseModel

class CreateContenidoDTO(BaseModel):
    titulo: str
    tipo: str
    clasificacion_edad: str


class UpdateContenidoDTO(BaseModel):
    titulo: str | None = None
    tipo: str | None = None
    clasificacion_edad: str | None = None


class DeleteContenidoDTO(BaseModel):
    id: int


class GetContenidoDTO(BaseModel):
    id: int


class ContenidoResponseDTO(BaseModel):
    id: int
    titulo: str
    tipo: int
    anio: int
    descripcion: str
    duracion_min: int
    clasificacion_edad: str


    model_config = {"from_attributes": True}
