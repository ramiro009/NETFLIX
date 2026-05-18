from datetime import datetime
from pydantic import BaseModel


class CreateContenidoIdiomasDTO(BaseModel):
    contenido_id: int
    idioma_id: int
    tipo: int


class UpdateContenidoIdiomasDTO(BaseModel):
    contenido_id: int | None = None
    idioma_id: int | None = None
    tipo: int | None = None


class DeleteContenidoIdiomasDTO(BaseModel):
    id: int


class GetContenidoIdiomasDTO(BaseModel):
    id: int


class ContenidoIdiomasResponseDTO(BaseModel):
    contenido_id: int
    idioma_id: int
    tipo: int 

    model_config = {"from_attributes": True}
