from datetime import datetime
from pydantic import BaseModel


class CreateContenidoIdiomasDTO(BaseModel):
    contenido_id: int
    idioma_id: int
    tipo: int


class ContenidoIdiomasResponseDTO(BaseModel):
    contenido_id: int
    idioma_id: int
    tipo: int 

    model_config = {"from_attributes": True}
