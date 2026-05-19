from pydantic import BaseModel, EmailStr, Field

class CreateCuentaSchema(BaseModel):
    email: EmailStr
    plan: str
    pin: str = Field(min_length=4, max_length=4)

class UpdateCuentaSchema(BaseModel):
    email: EmailStr | None = None
    plan: str | None = None
    pin: str | None = Field(None, min_length=4, max_length=4)
