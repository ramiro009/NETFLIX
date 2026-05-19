from pydantic import BaseModel, Field

class CreateGeneroSchema(BaseModel):
    nombre: str = Field(min_length=1, max_length=50)

class UpdateGeneroSchema(BaseModel):
    nombre: str | None = Field(None, min_length=1, max_length=50)
