from sqlalchemy.orm import Mapped
from sqlalchemy.orm import mapped_column

from .base import Base


class Worker(Base):

    fullname: Mapped[str] = mapped_column(unique=False)
    phone_number: Mapped[int] = mapped_column(unique=False)
    telegram_id: Mapped[int] = mapped_column(unique=False, nullable=True)
    status: Mapped[str] = mapped_column(unique=False)
