from pydantic import BaseModel, Field

class CreateContenidoIdiomaSchema(BaseModel):
    contenido_id: int
    idioma_id: int
    tipo: str = Field(description="Debe ser 'audio' o 'subtitulo'")

class UpdateContenidoIdiomaSchema(BaseModel):
    contenido_id: int | None = None
    idioma_id: int | None = None
    tipo: str | None = Field(None, description="Debe ser 'audio' o 'subtitulo'")