from src.db.models.vistas_model import Vistas
from src.dtos.vistas_dto import VisitasResponseDTO


def to_vista_response(vista: Vistas) -> VisitasResponseDTO:
    return VisitasResponseDTO.model_validate(vista)
