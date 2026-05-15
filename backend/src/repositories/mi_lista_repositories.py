from sqlalchemy.orm import Session
from src.db.models.cuentas_model import Cuentas


class CuentasRepository:
    def __init__(self, db: Session):
        self.db = db

    def create(self, email: str, plan: str, pin: str) -> Cuentas:
        cuenta = Cuentas(email=email, plan=plan, pin=pin)
        self.db.add(cuenta)
        self.db.commit()
        self.db.refresh(cuenta)
        return cuenta

    def find_by_id(self, cuenta_id: int) -> Cuentas | None:
        return self.db.query(Cuentas).filter(Cuentas.id == cuenta_id).first()

    def find_by_email(self, email: str) -> Cuentas | None:
        return self.db.query(Cuentas).filter(Cuentas.email == email).first()

    def list_all(self) -> list[Cuentas]:
        return self.db.query(Cuentas).all()

    def update(self, cuenta_id: int, email: str = None, plan: str = None, pin: str = None) -> Cuentas | None:
        cuenta = self.find_by_id(cuenta_id)
        if cuenta:
            if email is not None:
                cuenta.email = email
            if plan is not None:
                cuenta.plan = plan
            if pin is not None:
                cuenta.pin = pin
            self.db.commit()
        return cuenta

    def delete(self, cuenta_id: int) -> bool:
        cuenta = self.find_by_id(cuenta_id)
        if not cuenta:
            return False
        self.db.delete(cuenta)
        self.db.commit()
        return True