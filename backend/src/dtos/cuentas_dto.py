from datetime import datetime
from pydantic import BaseModel


class CreateCuentasDTO(BaseModel):
    email: str
    plan: str


class CuentasResponseDTO(BaseModel):
    id: int
    email: str
    plan: str
    pin: int
    fecha_alta: datetime

    model_config = {"from_attributes": True}
