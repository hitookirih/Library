from typing import TYPE_CHECKING

from sqlalchemy import String, DATETIME, ForeignKey
from sqlalchemy.orm import Mapped, relationship
from sqlalchemy.orm import mapped_column

from .base import Base
from .mixin.int_id_pk import IntIdPkMixin

if TYPE_CHECKING:
    from .books import Book


class Cover(IntIdPkMixin, Base):

    book_id: Mapped[int] = mapped_column(ForeignKey("books.id"))
    filename: Mapped[str] = mapped_column(String(255))
    storage_key: Mapped[str] = mapped_column(String(512))
    content_type: Mapped[str] = mapped_column(String(100))
    size: Mapped[int]

    book: Mapped["Book"] = relationship(back_populates="cover")
