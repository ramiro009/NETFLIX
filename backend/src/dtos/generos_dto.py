from datetime import datetime
from pydantic import BaseModel


class CreateGenerosDTO(BaseModel):
    nombre: str


class GenerosResponseDTO(BaseModel):
    id: int
    nombre: str

    model_config = {"from_attributes": True}
