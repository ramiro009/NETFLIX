from src.db.models.perfiles_model import Perfiles
from src.dtos.perfiles_dto import PerfilesResponseDTO


def to_perfil_response(perfil: Perfiles) -> PerfilesResponseDTO:
    return PerfilesResponseDTO.model_validate(perfil)

