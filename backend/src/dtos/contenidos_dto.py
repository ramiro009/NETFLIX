from datetime import datetime
from pydantic import BaseModel
from datetime import datetime

class CreateContenidoDTO(BaseModel):
    titulo: str
    tipo: str
    clasificacion_edad: str


class ContenidoResponseDTO(BaseModel):
    id: int
    titulo: str
    tipo: int
<<<<<<< HEAD

=======
>>>>>>> 2718d21c721260260ce71d1f1b217ab551d4954b
    anio: int
    descripcion: str
    duracion_min: int
    clasificacio_edad: str


    model_config = {"from_attributes": True}
