from datetime import datetime
from pydantic import BaseModel


class CreateTemporadasDTO(BaseModel):
    contenido_id: int
    numero: int
    anio: int


class TemporadasResponseDTO(BaseModel):
    id: int
    contenido_id: int
    numero: int
    anio: int
    created_at: datetime

    model_config = {"from_attributes": True}
