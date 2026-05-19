from pydantic import BaseModel, Field
from datetime import datetime

class CreateDescargasSchema(BaseModel):
    perfil_id: int
    contenido_id: int
    episodio_id: int | None = None
    vencimiento: datetime | None = None
    activa: bool = True

class UpdateDescargasSchema(BaseModel):
    perfil_id: int | None = None
    contenido_id: int | None = None
    episodio_id: int | None = None
    vencimiento: datetime | None = None
    activa: bool | None = None