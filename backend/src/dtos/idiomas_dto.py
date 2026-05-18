from datetime import datetime
from pydantic import BaseModel


class CreateIdiomasDTO(BaseModel):
    codigo: str
    nombre: str

class UpdateIdiomasDTO(BaseModel):
    codigo: str | None = None
    nombre: str | None = None


class DeleteIdiomasDTO(BaseModel):
    id: int


class GetIdiomasDTO(BaseModel):
    id: int



class IdiomasResponseDTO(BaseModel):
    id: int
    codigo: str
    nombre : str


    model_config = {"from_attributes": True}
