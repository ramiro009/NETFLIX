from datetime import datetime
from pydantic import BaseModel


class CreatePerfilesDTO(BaseModel):
    nombre: str
    es_infantil: bool
    avatar: str


class PerfilesResponseDTO(BaseModel):
    id: int
    cuenta_id: int
    nombre: str
    es_infantil: bool
    avatar: str
    bloqueado_hasta: datetime
    intentos_fallidos_pin: int


    model_config = {"from_attributes": True}
