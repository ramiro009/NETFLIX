from src.db.models.mi_lista_model import User
from src.dtos.mi_lista_dto import MiListaResponseDTO


def to_MiLista_response(MiLista: User) -> MiListaResponseDTO:
    return MiListaResponseDTO.model_validate(MiLista)
