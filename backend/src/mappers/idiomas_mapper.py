from src.db.models.idiomas_model import User
from src.dtos.idiomas_dto import IdiomasResponseDTO


def to_Idiomas_response(Idiomas: User) -> IdiomasResponseDTO:
    return IdiomasResponseDTO.model_validate(Idiomas)
