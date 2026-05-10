from datetime import datetime
from pydantic import BaseModel


class CreateUserDTO(BaseModel):
    username: str
    email: str
    password: str
    full_name: str


class UserResponseDTO(BaseModel):
    id: int
    username: str
    email: str
    full_name: str
    is_active: bool
    created_at: datetime
    updated_at: datetime

    model_config = {"from_attributes": True}
