from datetime import datetime
from pydantic import BaseModel

class CreateCuentasDTO(BaseModel):  
    email: str
    plan: str
    pin: int


class UpdateCuentasDTO(BaseModel):  
    email: str | None = None
    plan: str | None = None
    pin: int | None = None


class DeleteCuentasDTO(BaseModel):  
    id: int


class GetCuentasDTO(BaseModel):  
    id: int


class CuentasResponseDTO(BaseModel):
    id: int
    email: str
    plan: str
    pin: int
    fecha_alta: datetime

    model_config = {"from_attributes": True}