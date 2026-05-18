from datetime import datetime
from pydantic import BaseModel


class CreateDescargasDTO(BaseModel):
    perfil_id: int
    contenido_id: int
    episodio_id: int
    fecha_descarga: datetime


class UpdateDescargasDTO(BaseModel):
    perfil_id: int | None = None
    contenido_id: int | None = None
    episodio_id: int | None = None
    fecha_descarga: datetime | None = None


class DeleteDescargasDTO(BaseModel):
    id: int


class GetDescargasDTO(BaseModel):
    id: int


class DescargasResponseDTO(BaseModel):
    id: int
    perfil_id: int
    contenido_id: int
    episodio_id: int
    fecha_descarga: datetime


    model_config = {"from_attributes": True}
