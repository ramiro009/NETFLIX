from src.db.models.descargas_model import User
from src.dtos.descargas_dto import DescargasResponseDTO


def to_Descargas_response(Descargas: User) -> DescargasResponseDTO:
    return DescargasResponseDTO.model_validate(Descargas)
