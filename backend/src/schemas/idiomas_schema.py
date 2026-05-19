from pydantic import BaseModel, Field

class CreateIdiomaSchema(BaseModel):
    codigo: str = Field(min_length=2, max_length=2)
    nombre: str = Field(min_length=1, max_length=50)

class UpdateIdiomaSchema(BaseModel):
    codigo: str | None = Field(None, min_length=2, max_length=2)
    nombre: str | None = Field(None, min_length=1, max_length=50)