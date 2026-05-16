from sqlalchemy.orm import Session
from src.db.models.mi_lista_model import MiLista


class MiListaRepository:
    def __init__(self, db: Session):
        self.db = db

    def create(self, email: str, plan: str, pin: str) -> MiLista:
        mi_lista = MiLista(email=email, plan=plan, pin=pin)
        self.db.add(mi_lista)
        self.db.commit()
        self.db.refresh(mi_lista)
        return mi_lista

    def find_by_id(self, mi_lista_id: int) -> MiLista | None:
        return self.db.query(MiLista).filter(MiLista.id == mi_lista_id).first()

    def list_all(self) -> list[MiLista]:
        return self.db.query(MiLista).all()

    def update(self, mi_lista_id: int, email: str = None, plan: str = None, pin: str = None) -> MiLista | None:
        mi_lista = self.find_by_id(mi_lista_id)
        if mi_lista:
            if email is not None:
                mi_lista.email = email
            if plan is not None:
                mi_lista.plan = plan
            if pin is not None:
                mi_lista.pin = pin
            self.db.commit()
        return mi_lista

    def delete(self, mi_lista_id: int) -> bool:
        mi_lista = self.find_by_id(mi_lista_id)
        if not mi_lista:
            return False
        self.db.delete(mi_lista)
        self.db.commit()
        return True