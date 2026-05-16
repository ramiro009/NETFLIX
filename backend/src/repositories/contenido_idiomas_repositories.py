from sqlalchemy.orm import Session
from src.db.models.contenido_idiomas_model import ContenidoIdiomas


class ContenidoIdiomasRepository:
    def __init__(self, db: Session):
        self.db = db

    def create(self, email: str, plan: str, pin: str) -> ContenidoIdiomas:
        contenido_idioma = ContenidoIdiomas(email=email, plan=plan, pin=pin)
        self.db.add(contenido_idioma)
        self.db.commit()
        self.db.refresh(contenido_idioma)
        return contenido_idioma

    def find_by_id(self, contenido_idioma_id: int) -> ContenidoIdiomas | None:
        return self.db.query(ContenidoIdiomas).filter(ContenidoIdiomas.id == contenido_idioma_id).first()

    def list_all(self) -> list[ContenidoIdiomas]:
        return self.db.query(ContenidoIdiomas).all()

    def update(self, contenido_idioma_id: int, email: str = None, plan: str = None, pin: str = None) -> ContenidoIdiomas | None:
        contenido_idioma = self.find_by_id(contenido_idioma_id)
        if contenido_idioma:
            if email is not None:
                contenido_idioma.email = email
            if plan is not None:
                contenido_idioma.plan = plan
            if pin is not None:
                contenido_idioma.pin = pin
            self.db.commit()
        return contenido_idioma

    def delete(self, contenido_idioma_id: int) -> bool:
        contenido_idioma = self.find_by_id(contenido_idioma_id)
        if not contenido_idioma:
            return False
        self.db.delete(contenido_idioma)
        self.db.commit()
        return True