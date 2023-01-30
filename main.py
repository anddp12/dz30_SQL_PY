from sqlalchemy.orm import DeclarativeBase
from sqlalchemy.orm import Mapped
from sqlalchemy.orm import mapped_column
from sqlalchemy import create_engine


class Base(DeclarativeBase):
    pass

class Python23(Base):
    __tablename__ = "Students"

    id: Mapped[int] = mapped_column(primary_key=True, autoincrement=True)
    last_name: Mapped[str] = mapped_column()
    first_name: Mapped[str] = mapped_column()
    middle_name: Mapped[str] = mapped_column()
    stepcoin: Mapped[int] = mapped_column()
    diamonds: Mapped[int] = mapped_column()

    def __repr__(self) -> str:
        return f"Python23(id={self.id!r}, last_name={self.last_name!r}, first_name={self.first_name!r}, stepcoin={self.stepcoin!r}, first_name={self.diamonds!r})"

engine = create_engine("sqlite:///orm_db.db")