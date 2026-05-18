from datetime import datetime
from pydantic import BaseModel


class CreateCalificacionesDTO(BaseModel):
    perfil_id: int
    contenido_id: int
    puntaje: int
    fecha: datetime


class UpdateCalificacionesDTO(BaseModel):
    perfil_id: int | None = None
    contenido_id: int | None = None
    puntaje: int | None = None
    fecha: datetime | None = None


class DeleteCalificacionesDTO(BaseModel):
    id: int


class GetCalificacionesDTO(BaseModel):
    id: int


class CalificacionesResponseDTO(BaseModel):
    id: int
    perfil_id: int
    contenido_id: int
    puntaje: int
    fecha: datetime

    model_config = {"from_attributes": True}
