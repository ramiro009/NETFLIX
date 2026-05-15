from src.db.models.generos_model import Generos
from src.dtos.generos_dto import GenerosResponseDTO


def to_genero_response(genero: Generos) -> GenerosResponseDTO:
    return GenerosResponseDTO.model_validate(genero)
