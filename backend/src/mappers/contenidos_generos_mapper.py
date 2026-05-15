from src.db.models.contenido_generos_model import ContenidoGeneros
from src.dtos.contenidos_generos import ContenidoGenerosResponseDTO


def to_contenido_genero_response(contenido_genero: ContenidoGeneros) -> ContenidoGenerosResponseDTO:
    return ContenidoGenerosResponseDTO.model_validate(contenido_genero)

