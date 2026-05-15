from datetime import datetime
from pydantic import BaseModel


class CreateMiListaDTO(BaseModel):
    perfil_id: int
    contenidom_id: int
    fecha_agregada: datetime



class MiListaResponseDTO(BaseModel):
    id: int
    perfil_id: str
    contenido_id: int
    fecha_agregada: datetime

    model_config = {"from_attributes": True}
