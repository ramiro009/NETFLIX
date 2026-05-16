from sqlalchemy.orm import Session
from src.db.models.temporadas_model import Temporadas


class TemporadasRepository:
    def __init__(self, db: Session):
        self.db = db

    def create(self, contenido_id: int, numero: int, anio: int = None) -> Temporadas:
        temporada = Temporadas(contenido_id=contenido_id, numero=numero, anio=anio)
        self.db.add(temporada)
        self.db.commit()
        self.db.refresh(temporada)
        return temporada

    def find_by_id(self, temporada_id: int) -> Temporadas | None:
        return self.db.query(Temporadas).filter(Temporadas.id == temporada_id).first()

    def list_all(self) -> list[Temporadas]:
        return self.db.query(Temporadas).all()

    def update(self, temporada_id: int, numero: int = None, anio: int = None) -> Temporadas | None:
        temporada = self.find_by_id(temporada_id)
        if temporada:
            if numero is not None:
                temporada.numero = numero
            if anio is not None:
                temporada.anio = anio
            self.db.commit()
        return temporada

    def delete(self, temporada_id: int) -> bool:
        temporada = self.find_by_id(temporada_id)
        if not temporada:
            return False
        self.db.delete(temporada)
        self.db.commit()
        return True