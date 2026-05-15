from datetime import datetime
from pydantic import BaseModel


class CreateEpisodiosDTO(BaseModel):
    temporada_id: int
    numero: int
    titulo: str
    duracion_min: int



class EpisodiosResponseDTO(BaseModel):
    id: int
    temporada_id: str
    numero: int
    titulo: str
    duracion_min: int
    
    model_config = {"from_attributes": True}
