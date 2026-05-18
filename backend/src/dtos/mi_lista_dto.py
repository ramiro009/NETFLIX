from datetime import datetime
from pydantic import BaseModel


class CreateMiListaDTO(BaseModel):
    perfil_id: int
    contenido_id: int
    fecha_agregada: datetime

class UpdateMiListaDTO(BaseModel):
    perfil_id: int | None = None
    contenido_id: int | None = None
    fecha_agregada: datetime | None = None


class DeleteMiListaDTO(BaseModel):
    id: int


class GetMiListaDTO(BaseModel):
    id: int


class MiListaResponseDTO(BaseModel):
    perfil_id: int
    contenido_id: int
    fecha_agregada: datetime

    model_config = {"from_attributes": True}
