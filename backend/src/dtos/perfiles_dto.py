from datetime import datetime
from pydantic import BaseModel


class CreatePerfilesDTO(BaseModel):
    nombre: str
    es_infantil: bool
    avatar: str


class UpdatePerfilesDTO(BaseModel):
    nombre: str | None = None
    es_infantil: bool | None = None
    avatar: str | None = None
    bloqueado_hasta: datetime | None = None


class DeletePerfilesDTO(BaseModel):
    id: int


class GetPerfilesDTO(BaseModel):
    id: int


class PerfilesResponseDTO(BaseModel):
    id: int
    cuenta_id: int
    nombre: str
    es_infantil: bool
    avatar: str
    bloqueado_hasta: datetime
    intentos_fallidos_pin: int

    model_config = {"from_attributes": True}
