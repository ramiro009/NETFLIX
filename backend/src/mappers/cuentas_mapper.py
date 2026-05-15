from src.db.models.cuentas_model import User
from src.dtos.cuentas_dto import CuentasResponseDTO


def to_cuenta_response(cuenta: User) -> CuentasResponseDTO:
    return CuentasResponseDTO.model_validate(cuenta)
