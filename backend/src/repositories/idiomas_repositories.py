from sqlalchemy.orm import Session
from src.db.models.idiomas_model import Idiomas


class IdiomasRepository:
    def __init__(self, db: Session):
        self.db = db

    def create(self, codigo: str, nombre: str) -> Idiomas:
        idioma = Idiomas(codigo=codigo, nombre=nombre)
        self.db.add(idioma)
        self.db.commit()
        self.db.refresh(idioma)
        return idioma

    def find_by_id(self, idioma_id: int) -> Idiomas | None:
        return self.db.query(Idiomas).filter(Idiomas.id == idioma_id).first()

    def list_all(self) -> list[Idiomas]:
        return self.db.query(Idiomas).all()

    def update(self, idioma_id: int, codigo: str = None, nombre: str = None) -> Idiomas | None:
        idioma = self.find_by_id(idioma_id)
        if idioma:
            if codigo is not None:
                idioma.codigo = codigo
            if nombre is not None:
                idioma.nombre = nombre
            self.db.commit()
        return idioma

    def delete(self, idioma_id: int) -> bool:
        idioma = self.find_by_id(idioma_id)
        if not idioma:
            return False
        self.db.delete(idioma)
        self.db.commit()
        return True