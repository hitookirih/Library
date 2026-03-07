from typing import TYPE_CHECKING

from sqlalchemy import String
from sqlalchemy.orm import Mapped, relationship
from sqlalchemy.orm import mapped_column

from .base import Base

if TYPE_CHECKING:
    from .covers import Cover


class Book(Base):

    title: Mapped[str] = mapped_column(unique=False)
    author: Mapped[str] = mapped_column(unique=False)
    description: Mapped[str] = mapped_column(String(300), unique=False, nullable=True)

    cover: Mapped["Cover"] = relationship(back_populates="book")
