from sqlalchemy.orm import Session

from src.db.models.user_model import User


class UserRepository:
    def __init__(self, db: Session):
        self.db = db

    def create(self, email: str, password_hash: str, age: int) -> User:
        user = User(email=email, password_hash=password_hash, age=age)
        self.db.add(user)
        self.db.commit()
        self.db.refresh(user)
        return user

    def find_by_id(self, user_id: int) -> User | None:
        return self.db.query(User).filter(User.id == user_id).first()

    def find_by_email(self, email: str) -> User | None:
        return self.db.query(User).filter(User.email == email).first()

    def list_all(self) -> list[User]:
        return self.db.query(User).all()

    def update(self, user_id: int, email: str = None, password_hash: str = None, age: int = None):
        user = self.find_by_id(user_id)
        if user:
            if email is not None:
                user.email = email
            if password_hash is not None:
                user.password_hash = password_hash
            if age is not None:
                user.age = age
            self.db.commit()
        return user

    def delete(self, user_id: int) -> bool:
        user = self.find_by_id(user_id)
        if not user:
            return False
        self.db.delete(user)
        self.db.commit()
        return True