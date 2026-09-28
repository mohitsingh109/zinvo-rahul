import uuid

from sqlalchemy.orm import Session

from app.models.user import User


def create(db: Session, user: User) -> User:
    # insert into users (id, email, hashed_password, is_active, created_at, updated_at) values (...)
    db.add(user) # ORM (class object convert sql query)
    db.commit() # call DB save
    db.refresh(user) # fetching the later record from DB
    return user


def get_by_id(db: Session, user_id: uuid.UUID) -> User | None:
    # select * from user where user_id = ?
    return db.get(User, user_id) # Sql query to object
# db.get(<Class Name/Schema>, <pk value>)


def get_by_email(db: Session, email: str) -> User | None:
    # db.query always return an array
    # select * from user where email = ? limit 1
    return db.query(User).filter(User.email == email).first()

# first 100: skip: 0 limit 100
# next 100: skip: 100 limit 100
def list(db: Session, skip: int = 0, limit: int = 100) -> list[User]:
    return db.query(User).offset(skip).limit(limit).all()


def update(db: Session, user: User) -> User:
    db.commit()
    db.refresh(user)
    return user


def delete(db: Session, user: User) -> None:
    db.delete(user) # operation
    db.commit() # perform
