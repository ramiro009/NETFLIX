from datetime import datetime
from pydantic import BaseModel


class CreateContenidoGenerosDTO(BaseModel):
    contenido_id: int
    genero_id: int


class UpdateContenidoGenerosDTO(BaseModel):
    contenido_id: int | None = None
    genero_id: int | None = None


class DeleteContenidoGenerosDTO(BaseModel):
    id: int


class GetContenidoGenerosDTO(BaseModel):
    id: int


class ContenidoGenerosResponseDTO(BaseModel):
    contenido_id: int
    genero_id: int
    

    model_config = {"from_attributes": True}
