from sqlalchemy.orm import Session
from src.db.models.perfiles_model import Perfiles


class PerfilesRepository:
    def __init__(self, db: Session):
        self.db = db

    def create(self, email: str, plan: str, pin: str) -> Perfiles:
        perfil = Perfiles(email=email, plan=plan, pin=pin)
        self.db.add(perfil)
        self.db.commit()
        self.db.refresh(perfil)
        return perfil

    def find_by_id(self, perfil_id: int) -> Perfiles | None:
        return self.db.query(Perfiles).filter(Perfiles.id == perfil_id).first()

    def list_all(self) -> list[Perfiles]:
        return self.db.query(Perfiles).all()

    def update(self, perfil_id: int, email: str = None, plan: str = None, pin: str = None) -> Perfiles | None:
        perfil = self.find_by_id(perfil_id)
        if perfil:
            if email is not None:
                perfil.email = email
            if plan is not None:
                perfil.plan = plan
            if pin is not None:
                perfil.pin = pin
            self.db.commit()
        return perfil

    def delete(self, perfil_id: int) -> bool:
        perfil = self.find_by_id(perfil_id)
        if not perfil:
            return False
        self.db.delete(perfil)
        self.db.commit()
        return True