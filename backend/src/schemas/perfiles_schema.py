from pydantic import BaseModel, Field

class CreatePerfilSchema(BaseModel):
    nombre: str = Field(min_length=1, max_length=50)
    es_infantil: bool = False
    avatar: str | None = None

class UpdatePerfilSchema(BaseModel):
    nombre: str | None = Field(None, min_length=1, max_length=50)
    es_infantil: bool | None = None
    avatar: str | None = None
