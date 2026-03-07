from sqlalchemy.orm import Mapped
from sqlalchemy.orm import mapped_column

from .base import Base


class Worker(Base):

    fullname: Mapped[str] = mapped_column(Unique=False)
    phone_number: Mapped[int] = mapped_column(Unique=False)
    telegram_id: Mapped[int] = mapped_column(Unique=False)
