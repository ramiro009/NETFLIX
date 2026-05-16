from sqlalchemy.orm import Session
from src.db.models.generos_model import Generos


class GenerosRepository:
    def __init__(self, db: Session):
        self.db = db

    def create(self, nombre: str) -> Generos:
        genero = Generos(nombre=nombre)
        self.db.add(genero)
        self.db.commit()
        self.db.refresh(genero)
        return genero

    def find_by_id(self, genero_id: int) -> Generos | None:
        return self.db.query(Generos).filter(Generos.id == genero_id).first()

    def list_all(self) -> list[Generos]:
        return self.db.query(Generos).all()

    def update(self, genero_id: int, nombre: str = None) -> Generos | None:
        genero = self.find_by_id(genero_id)
        if genero:
            if nombre is not None:
                genero.nombre = nombre
            self.db.commit()
        return genero

    def delete(self, genero_id: int) -> bool:
        genero = self.find_by_id(genero_id)
        if not genero:
            return False
        self.db.delete(genero)
        self.db.commit()
        return True