from datetime import datetime
from pydantic import BaseModel


class CreateDescargasDTO(BaseModel):
    perfil_id: int
    contenido_id: int
    episodio_id: int
    fecha_descarga: datetime


class DescargasResponseDTO(BaseModel):
    id: int
    perfil_id: str
    contenido_id: int
    episodio_id: int
    fecha_descarga: datetime


    model_config = {"from_attributes": True}
