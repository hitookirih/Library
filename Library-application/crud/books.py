from typing import Sequence, Annotated

from sqlalchemy import select
from sqlalchemy.ext.asyncio import AsyncSession

from fastapi import Path, Depends, HTTPException, status

from core.models import Book, db_helper
from core.schemas.book import BookCreate, BookUpdate, BookUpdatePartial


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


async def book_by_id(
    book_id: Annotated[int, Path],
    session: AsyncSession = Depends(db_helper.session_getter),
) -> Book | None:
    book = await get_book(session=session, book_id=book_id)
    if book is not None:
        return book
    raise HTTPException(
        status_code=status.HTTP_404_NOT_FOUND, detail=f"Book {book_id} not found!"
    )


async def update_book(
    session: AsyncSession,
    book: Book,
    book_update: BookUpdate | BookUpdatePartial,
    partial: bool = False,
) -> Book:
    for name, value in book_update.model_dump(exclude_unset=partial).items():
        setattr(book, name, value)
        await session.commit()
    return book


async def delete_book(session: AsyncSession, book: Book) -> None:
    await session.delete(book)
    await session.commit()
