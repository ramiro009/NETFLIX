from pydantic import BaseModel, Field

class CreateEpisodioSchema(BaseModel):
    temporada_id: int
    numero: int = Field(ge=1)
    titulo: str = Field(min_length=1, max_length=255)
    duracion_min: int = Field(ge=1)
    descripcion: str | None = None

class UpdateEpisodioSchema(BaseModel):
    temporada_id: int | None = None
    numero: int | None = Field(None, ge=1)
    titulo: str | None = Field(None, min_length=1, max_length=255)
    duracion_min: int | None = Field(None, ge=1)
    descripcion: str | None = None
