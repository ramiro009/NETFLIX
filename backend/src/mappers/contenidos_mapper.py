from src.db.models.contenidos_model import Contenido
from src.dtos.contenidos_dto import ContenidoResponseDTO


def to_contenido_response(contenido: Contenido) -> ContenidoResponseDTO:
    return ContenidoResponseDTO.model_validate(contenido)
