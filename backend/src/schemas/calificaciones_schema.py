from pydantic import BaseModel, Field

class CreateCalificacionSchema(BaseModel):
    perfil_id: int
    contenido_id: int
    puntaje: int = Field(ge=1, le=5)

class UpdateCalificacionSchema(BaseModel):
    perfil_id: int | None = None
    contenido_id: int | None = None
    puntaje: int | None = Field(None, ge=1, le=5)