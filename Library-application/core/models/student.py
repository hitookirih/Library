from sqlalchemy.orm import Mapped
from sqlalchemy.orm import mapped_column

from .base import Base
from .mixin.int_id_pk import IntIdPkMixin


class Student(IntIdPkMixin, Base):
    number_of_studak: Mapped[int] = mapped_column(unique=True)
    number_of_group: Mapped[str] = mapped_column(unique=False)
    name: Mapped[str] = mapped_column(unique=False)
    surname: Mapped[str] = mapped_column(unique=False)
    father_name: Mapped[str] = mapped_column(unique=False)
    phone_number: Mapped[int] = mapped_column(unique=True)
    telegram_id: Mapped[str] = mapped_column(unique=True)
    status: Mapped[str] = mapped_column(unique=False)
