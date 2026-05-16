from sqlalchemy.orm import Session
from src.db.models.calificaciones_model import Calificaciones


class CalificacionesRepository:
    def __init__(self, db: Session):
        self.db = db

    def create(self, email: str, plan: str, pin: str) -> Calificaciones:
        calificacion = Calificaciones(email=email, plan=plan, pin=pin)
        self.db.add(calificacion)
        self.db.commit()
        self.db.refresh(calificacion)
        return calificacion

    def find_by_id(self, calificacion_id: int) -> Calificaciones | None:
        return self.db.query(Calificaciones).filter(Calificaciones.id == calificacion_id).first()

    def list_all(self) -> list[Calificaciones]:
        return self.db.query(Calificaciones).all()

    def update(self, calificacion_id: int, email: str = None, plan: str = None, pin: str = None) -> Calificaciones | None:
        calificacion = self.find_by_id(calificacion_id)
        if calificacion:
            if email is not None:
                calificacion.email = email
            if plan is not None:
                calificacion.plan = plan
            if pin is not None:
                calificacion.pin = pin
            self.db.commit()
        return calificacion

    def delete(self, calificacion_id: int) -> bool:
        calificacion = self.find_by_id(calificacion_id)
        if not calificacion:
            return False
        self.db.delete(calificacion)
        self.db.commit()
        return True