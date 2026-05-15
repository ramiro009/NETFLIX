from src.db.models.temporadas_model import Temporadas
from src.dtos.temporadas_dto import TemporadasResponseDTO


def to_temporada_response(temporada: Temporadas) -> TemporadasResponseDTO:
    return TemporadasResponseDTO.model_validate(temporada)
