from datetime import datetime
from pydantic import BaseModel


class CreateVisitasDTO(BaseModel):
    perfil_id: int
    contenido_id: int
    episodio_id: int
    fecha: datetime
    segundos_vistos: int
    terminados: bool


class VisitasResponseDTO(BaseModel):
    id: int
    perfil_id: int
    contenido_id: int
    episodio_id: int
    fecha: datetime
    segundos_vistos: int
    terminados: bool


    model_config = {"from_attributes": True}
