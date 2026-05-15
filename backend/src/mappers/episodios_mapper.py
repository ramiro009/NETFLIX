from src.db.models.episodios_model import Episodios
from src.dtos.empisodios_dto import EpisodiosResponseDTO


def to_episodio_response(episodio: Episodios) -> EpisodiosResponseDTO:
    return EpisodiosResponseDTO.model_validate(episodio)
