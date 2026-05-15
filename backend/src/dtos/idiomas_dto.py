from datetime import datetime
from pydantic import BaseModel


class CreateIdiomasDTO(BaseModel):
    codigo: str
    nombre: str



class IdiomasResponseDTO(BaseModel):
    id: int
    codigo: str
    nombre : str


    model_config = {"from_attributes": True}
