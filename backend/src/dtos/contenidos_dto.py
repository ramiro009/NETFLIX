from pydantic import BaseModel


class CreateContenidoDTO(BaseModel):
    titulo: str
    tipo: str
    clasificacion_edad: str


class ContenidoResponseDTO(BaseModel):
    id: int
    titulo: str
    tipo: str
    anio: int
    descripcion: str
    duracion_min: int
    clasificacion_edad: str

    model_config = {"from_attributes": True}
