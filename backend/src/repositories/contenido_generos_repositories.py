from sqlalchemy.orm import Session
from src.db.models.contenido_generos_model import ContenidoGeneros


class ContenidoGenerosRepository:
    def __init__(self, db: Session):
        self.db = db

    def create(self, email: str, plan: str, pin: str) -> ContenidoGeneros:
        contenido_genero = ContenidoGeneros(email=email, plan=plan, pin=pin)
        self.db.add(contenido_genero)
        self.db.commit()
        self.db.refresh(contenido_genero)
        return contenido_genero

    def find_by_id(self, contenido_genero_id: int) -> ContenidoGeneros | None:
        return self.db.query(ContenidoGeneros).filter(ContenidoGeneros.id == contenido_genero_id).first()

    def list_all(self) -> list[ContenidoGeneros]:
        return self.db.query(ContenidoGeneros).all()

    def update(self, contenido_genero_id: int, email: str = None, plan: str = None, pin: str = None) -> ContenidoGeneros | None:
        contenido_genero = self.find_by_id(contenido_genero_id)
        if contenido_genero:
            if email is not None:
                contenido_genero.email = email
            if plan is not None:
                contenido_genero.plan = plan
            if pin is not None:
                contenido_genero.pin = pin
            self.db.commit()
        return contenido_genero

    def delete(self, contenido_genero_id: int) -> bool:
        contenido_genero = self.find_by_id(contenido_genero_id)
        if not contenido_genero:
            return False
        self.db.delete(contenido_genero)
        self.db.commit()
        return True