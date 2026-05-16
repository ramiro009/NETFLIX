from sqlalchemy.orm import Session
from src.db.models.visitas_model import Visitas


class VisitasRepository:
    def __init__(self, db: Session):
        self.db = db

    def create(self, email: str, plan: str, pin: str) -> Visitas:
        visita = Visitas(email=email, plan=plan, pin=pin)
        self.db.add(visita)
        self.db.commit()
        self.db.refresh(visita)
        return visita

    def find_by_id(self, visita_id: int) -> Visitas | None:
        return self.db.query(Visitas).filter(Visitas.id == visita_id).first()

    def list_all(self) -> list[Visitas]:
        return self.db.query(Visitas).all()

    def update(self, visita_id: int, email: str = None, plan: str = None, pin: str = None) -> Visitas | None:
        visita = self.find_by_id(visita_id)
        if visita:
            if email is not None:
                visita.email = email
            if plan is not None:
                visita.plan = plan
            if pin is not None:
                visita.pin = pin
            self.db.commit()
        return visita

    def delete(self, visita_id: int) -> bool:
        visita = self.find_by_id(visita_id)
        if not visita:
            return False
        self.db.delete(visita)
        self.db.commit()
        return True