from datetime import datetime
from pydantic import BaseModel


class CreateGenerosDTO(BaseModel):
    nombre: str


class UpdateGenerosDTO(BaseModel):
    nombre: str | None = None


class DeleteGenerosDTO(BaseModel):
    id: int


class GetGenerosDTO(BaseModel):
    id: int


class GenerosResponseDTO(BaseModel):
    id: int
    nombre: str

    model_config = {"from_attributes": True}
