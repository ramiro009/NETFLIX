from datetime import datetime
from pydantic import BaseModel


class CreateVisitasDTO(BaseModel):
    perfil_id: int
    contenido_id: int
    episodio_id: int
    fecha: datetime
    segundos_vistos: int
    terminados: bool


class UpdateVisitasDTO(BaseModel):
    perfil_id: int | None = None
    contenido_id: int | None = None
    episodio_id: int | None = None
    fecha: datetime | None = None
    segundos_vistos: int | None = None
    terminados: bool | None = None


class DeleteVisitasDTO(BaseModel):
    id: int


class GetVisitasDTO(BaseModel):
    id: int


class VisitasResponseDTO(BaseModel):
    id: int
    perfil_id: int
    contenido_id: int
    episodio_id: int
    fecha: datetime
    segundos_vistos: int
    terminados: bool


    model_config = {"from_attributes": True}
