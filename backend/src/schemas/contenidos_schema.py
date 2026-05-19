from pydantic import BaseModel, Field

class CreateContenidoSchema(BaseModel):
    titulo: str = Field(min_length=1, max_length=255)
    tipo: str
    anio: int
    descripcion: str
    duracion_min: int
    clasificacion_edad: str

class UpdateContenidoSchema(BaseModel):
    titulo: str | None = Field(None, min_length=1, max_length=255)
    tipo: str | None = None
    anio: int | None = None
    descripcion: str | None = None
    duracion_min: int | None = None
    clasificacion_edad: str | None = None