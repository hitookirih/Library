from typing import Sequence

from sqlalchemy import select
from sqlalchemy.ext.asyncio import AsyncSession

from core.models import Book
from core.schemas.book import BookCreate


async def get_book(session: AsyncSession, book_id: int) -> Book | None:
    return await session.get(Book, book_id)


async def get_all_books(
    session: AsyncSession,
) -> Sequence[Book]:
    stmt = select(Book).order_by(Book.id)
    result = await session.scalars(stmt)
    return result.all()


async def create_book(
    session: AsyncSession,
    book_create: BookCreate,
) -> Book:
    book = Book(**book_create.model_dump())
    session.add(book)
    await session.commit()
    await session.refresh(book)
    return book
