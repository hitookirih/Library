from sqlalchemy.orm import Mapped
from sqlalchemy.orm import mapped_column

from .base import Base


class Student(Base):
    number_of_studak: Mapped[int] = mapped_column(unique=True)
    number_of_group: Mapped[str] = mapped_column(unique=False)
    name: Mapped[str] = mapped_column(unique=False)
    fullname: Mapped[str] = mapped_column(unique=False)
    father_name: Mapped[str] = mapped_column(unique=False)
    phone_number: Mapped[int] = mapped_column(unique=True)
    telegram_id: Mapped[str] = mapped_column(unique=True)
    status: Mapped[str] = mapped_column(unique=False)
