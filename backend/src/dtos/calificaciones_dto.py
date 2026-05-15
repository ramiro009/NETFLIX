from datetime import datetime
from pydantic import BaseModel


class CreateCalificacionesDTO(BaseModel):
    perfil_id: int
    contenido_id: int
    puntaje: int
    fecha: datetime


class CalificacionesResponseDTO(BaseModel):
    id: int
    perfil_id: int
    contenido_id: int
    puntaje: int
    fecha: datetime

    model_config = {"from_attributes": True}
