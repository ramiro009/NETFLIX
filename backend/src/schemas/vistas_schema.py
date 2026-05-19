from pydantic import BaseModel, Field

class CreateVistaSchema(BaseModel):
    perfil_id: int
    episodio_id: int
    segundos_vistos: int = Field(ge=0)
    terminado: bool = False

class UpdateVistaSchema(BaseModel):
    perfil_id: int | None = None
    episodio_id: int | None = None
    segundos_vistos: int | None = Field(None, ge=0)
    terminado: bool | None = None