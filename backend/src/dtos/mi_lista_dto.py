from datetime import datetime
from pydantic import BaseModel


class CreateUserDTO(BaseModel):
    perfil_id: int
    contenidom_id: int
    fecha_agregada: datetime



class UserResponseDTO(BaseModel):
    id: int
    perfil_id: str
    contenido_id: int
    fecha_agregada: datetime

    model_config = {"from_attributes": True}
