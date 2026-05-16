from sqlalchemy.orm import Session
from src.db.models.episodios_model import Episodios


class EpisodiosRepository:
    def __init__(self, db: Session):
        self.db = db

    def create(self, temporada_id: int, numero: int, titulo: str, duracion_min: int) -> Episodios:
        episodio = Episodios(temporada_id=temporada_id, numero=numero, titulo=titulo, duracion_min=duracion_min)
        self.db.add(episodio)
        self.db.commit()
        self.db.refresh(episodio)
        return episodio

    def find_by_id(self, episodio_id: int) -> Episodios | None:
        return self.db.query(Episodios).filter(Episodios.id == episodio_id).first()

    def list_all(self) -> list[Episodios]:
        return self.db.query(Episodios).all()

    def update(self, episodio_id: int, numero: int = None, titulo: str = None, duracion_min: int = None) -> Episodios | None:
        episodio = self.find_by_id(episodio_id)
        if episodio:
            if numero is not None:
                episodio.numero = numero
            if titulo is not None:
                episodio.titulo = titulo
            if duracion_min is not None:
                episodio.duracion_min = duracion_min
            self.db.commit()
        return episodio

    def delete(self, episodio_id: int) -> bool:
        episodio = self.find_by_id(episodio_id)
        if not episodio:
            return False
        self.db.delete(episodio)
        self.db.commit()
        return True