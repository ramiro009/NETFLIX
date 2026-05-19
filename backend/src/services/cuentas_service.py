from sqlalchemy.orm import Session

from src.dtos.cuentas_dto import CreateCuentasDTO, UpdateCuentasDTO, CuentasResponseDTO
from src.mappers.cuentas_mapper import to_cuenta_response
from src.repositories.cuentas_repositories import CuentasRepository
from src.utils.errors import NotFoundError


class CuentasService:
    def __init__(self, db: Session):
        self.repo = CuentasRepository(db)

    def create(self, dto: CreateCuentasDTO) -> CuentasResponseDTO:
        cuenta = self.repo.create(
            email=dto.email,
            plan=dto.plan,
            pin=str(dto.pin),
        )
        return to_cuenta_response(cuenta)

    def get_by_id(self, cuenta_id: int) -> CuentasResponseDTO:
        cuenta = self.repo.find_by_id(cuenta_id)
        if not cuenta:
            raise NotFoundError(f"Cuenta con id {cuenta_id} no encontrada")
        return to_cuenta_response(cuenta)

    def list_all(self) -> list[CuentasResponseDTO]:
        cuentas = self.repo.list_all()
        return [to_cuenta_response(c) for c in cuentas]

    def update(self, cuenta_id: int, dto: UpdateCuentasDTO) -> CuentasResponseDTO:
        cuenta = self.repo.update(
            cuenta_id=cuenta_id,
            email=dto.email,
            plan=dto.plan,
            pin=str(dto.pin) if dto.pin is not None else None,
        )
        if not cuenta:
            raise NotFoundError(f"Cuenta con id {cuenta_id} no encontrada")
        return to_cuenta_response(cuenta)

    def delete(self, cuenta_id: int) -> None:
        success = self.repo.delete(cuenta_id)
        if not success:
            raise NotFoundError(f"Cuenta con id {cuenta_id} no encontrada")
