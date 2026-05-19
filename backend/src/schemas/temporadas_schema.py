from pydantic import BaseModel, Field

class CreateTemporadaSchema(BaseModel):
    contenido_id: int
    numero: int = Field(ge=1)
    anio: int

class UpdateTemporadaSchema(BaseModel):
    contenido_id: int | None = None
    numero: int | None = Field(None, ge=1)
    anio: int | None = None
