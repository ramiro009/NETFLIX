from sqlalchemy.orm import Session
from src.db.models.descargas_model import Descargas


class DescargasRepository:
    def __init__(self, db: Session):
        self.db = db

    def create(self, email: str, plan: str, pin: str) -> Descargas:
        descarga = Descargas(email=email, plan=plan, pin=pin)
        self.db.add(descarga)
        self.db.commit()
        self.db.refresh(descarga)
        return descarga

    def find_by_id(self, descarga_id: int) -> Descargas | None:
        return self.db.query(Descargas).filter(Descargas.id == descarga_id).first()

    def list_all(self) -> list[Descargas]:
        return self.db.query(Descargas).all()

    def update(self, descarga_id: int, email: str = None, plan: str = None, pin: str = None) -> Descargas | None:
        descarga = self.find_by_id(descarga_id)
        if descarga:
            if email is not None:
                descarga.email = email
            if plan is not None:
                descarga.plan = plan
            if pin is not None:
                descarga.pin = pin
            self.db.commit()
        return descarga

    def delete(self, descarga_id: int) -> bool:
        descarga = self.find_by_id(descarga_id)
        if not descarga:
            return False
        self.db.delete(descarga)
        self.db.commit()
        return True