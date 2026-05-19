from pydantic import BaseModel, EmailStr, Field


class CreateUserSchema(BaseModel):
    email: EmailStr
    password: str = Field(min_length=8)
    age: int


class UpdateUserSchema(BaseModel):
    email: EmailStr | None = None
    password: str | None = Field(None, min_length=8)
    age: int | None = None
