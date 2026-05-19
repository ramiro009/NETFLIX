from pydantic import BaseModel

class CreateContenidoGeneroSchema(BaseModel):
    contenido_id: int
    genero_id: int

class UpdateContenidoGeneroSchema(BaseModel):
    contenido_id: int | None = None
    genero_id: int | None = None