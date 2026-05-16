from sqlalchemy.orm import Session
from src.db.models.contenidos_model import Contenidos


class ContenidosRepository:
    def __init__(self, db: Session):
        self.db = db

    def create(self, titulo: str, tipo: str, anio: int, descripcion: str, duracion_min: int, clasificacion_edad: str) -> Contenidos:
        contenido = Contenidos(
            titulo=titulo, 
            tipo=tipo, 
            anio=anio, 
            descripcion=descripcion, 
            duracion_min=duracion_min, 
            clasificacion_edad=clasificacion_edad
        )
        self.db.add(contenido)
        self.db.commit()
        self.db.refresh(contenido)
        return contenido

    def find_by_id(self, contenido_id: int) -> Contenidos | None:
        return self.db.query(Contenidos).filter(Contenidos.id == contenido_id).first()

    def list_all(self) -> list[Contenidos]:
        return self.db.query(Contenidos).all()

    def update(self, contenido_id: int, titulo: str = None, descripcion: str = None, clasificacion_edad: str = None) -> Contenidos | None:
        contenido = self.find_by_id(contenido_id)
        if contenido:
            if titulo is not None:
                contenido.titulo = titulo
            if descripcion is not None:
                contenido.descripcion = descripcion
            if clasificacion_edad is not None:
                contenido.clasificacion_edad = clasificacion_edad
            self.db.commit()
        return contenido

    def delete(self, contenido_id: int) -> bool:
        contenido = self.find_by_id(contenido_id)
        if not contenido:
            return False
        self.db.delete(contenido)
        self.db.commit()
        return True