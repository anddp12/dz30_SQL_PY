from sqlalchemy.orm import DeclarativeBase
from sqlalchemy.orm import Mapped
from sqlalchemy.orm import mapped_column
from sqlalchemy import create_engine
from sqlalchemy.orm import Session
from sqlalchemy import desc


class Base(DeclarativeBase):
    pass

class Python23(Base):
    __tablename__ = "Students"

    id: Mapped[int] = mapped_column(primary_key=True, autoincrement=True)
    last_name: Mapped[str] = mapped_column()
    first_name: Mapped[str] = mapped_column()
    middle_name: Mapped[str] = mapped_column()
    stepcoin: Mapped[int] = mapped_column()

    def __repr__(self) -> str:
        return f"Python23(id={self.id!r}, last_name={self.last_name!r}, first_name={self.first_name!r}, stepcoin={self.stepcoin!r})"

engine = create_engine("sqlite:///orm_db.db")

Base.metadata.drop_all(engine)
Base.metadata.create_all(engine)

with Session(engine) as session:
    student1 = Python23(last_name="Ярошкін", first_name="Сергій", middle_name="Сергійович", stepcoin=529)
    student2 = Python23(last_name="Таран", first_name="Андрій", middle_name="Ігорович", stepcoin=527)
    student3 = Python23(last_name="Бєлоусов", first_name="Юрій", middle_name="Володимирович", stepcoin=480)
    student4 = Python23(last_name="Марченко", first_name="Ілля", middle_name="Андрійович", stepcoin=430)
    student5 = Python23(last_name="Зайченко", first_name="Михайло", middle_name="Андрійович", stepcoin=419)
    student6 = Python23(last_name="Діденко", first_name="Нікіта", middle_name="Сергійович", stepcoin=301)
    student7 = Python23(last_name="Лозовий", first_name="Олексій", middle_name="Андрійович", stepcoin=293)
    student8 = Python23(last_name="Ахмедов", first_name="Ахмед", middle_name="Анар Огли", stepcoin=263)
    student9 = Python23(last_name="Рыжков", first_name="Владислав", middle_name="Андреевич", stepcoin=226)
    student10 = Python23(last_name="Каштаєв", first_name="Артур", middle_name="Віталійович", stepcoin=225)
    student11 = Python23(last_name="Тараканов", first_name="Сергій", middle_name="Михайлович", stepcoin=197)
    student12 = Python23(last_name="Стрельченко", first_name="Дмитро", middle_name="Олександрович", stepcoin=162)

session.add_all([student1, student2, student3, student4, student5, student6, student7, student8, student9, student10, student11, student12])
session.commit()

# Удалить студентов у которых рейтинг рейтинг меньше заданного значения (любое число)
delete = session.query(Python23).filter(Python23.id > 10).limit(5).all()
print(delete)
for i in delete:
    session.delete(i)
    session.commit()

# Увеличить в своей записи рейтинг на 5 ед.
student2.stepcoin = 533
print(student2)
session.commit()
