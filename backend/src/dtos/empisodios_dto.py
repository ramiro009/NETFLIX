from datetime import datetime
from pydantic import BaseModel


class CreateEpisodiosDTO(BaseModel):
    temporada_id: int
    numero: int
    titulo: str
    duracion_min: int


class UpdateEpisodiosDTO(BaseModel):
    temporada_id: int | None = None
    numero: int | None = None
    titulo: str | None = None
    duracion_min: int | None = None


class DeleteEpisodiosDTO(BaseModel):
    id: int


class GetEpisodiosDTO(BaseModel):
    id: int


class EpisodiosResponseDTO(BaseModel):
    id: int
    temporada_id: int
    numero: int
    titulo: str
    duracion_min: int
    
    model_config = {"from_attributes": True}
