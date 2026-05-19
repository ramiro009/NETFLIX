from pydantic import BaseModel

class CreateMiListaSchema(BaseModel):
    perfil_id: int
    contenido_id: int

class UpdateMiListaSchema(BaseModel):
    perfil_id: int | None = None
    contenido_id: int | None = None