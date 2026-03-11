from typing import Annotated

from fastapi import APIRouter, Depends, status
from sqlalchemy.ext.asyncio import AsyncSession

from core.models import db_helper, Book
from core.schemas.book import BookRead, BookCreate, BookUpdate
from crud import books as books_crud
from crud.books import update_book, book_by_id, delete_book

router = APIRouter(tags=["Books"])


@router.get("/", response_model=list[BookRead])
async def get_books(
    session: Annotated[
        AsyncSession,
        Depends(db_helper.session_getter),
    ],
):
    books = await books_crud.get_all_books(session=session)
    return books


@router.post("", response_model=BookRead, status_code=status.HTTP_201_CREATED)
async def create_book(
    session: Annotated[
        AsyncSession,
        Depends(db_helper.session_getter),
    ],
    book_create: BookCreate,
):
    book = await books_crud.create_book(
        session=session,
        book_create=book_create,
    )
    return book


@router.get("{book_id}", response_model=BookRead)
async def get_book_by_id(
    book: Book = Depends(book_by_id),
) -> Book:
    return book


@router.put("{book_id}", response_model=BookRead)
async def view_book_update(
    session: Annotated[AsyncSession, Depends(db_helper.session_getter)],
    book_update: BookUpdate,
    book: Book = Depends(book_by_id),
) -> Book:
    return await update_book(
        session=session,
        book=book,
        book_update=book_update,
    )


@router.patch("{book_id}", response_model=BookRead)
async def view_book_update_partial(
    session: Annotated[AsyncSession, Depends(db_helper.session_getter)],
    book_update: BookUpdate,
    book: Book = Depends(book_by_id),
) -> Book:
    return await update_book(
        session=session,
        book=book,
        book_update=book_update,
        partial=True,
    )


@router.delete("{book_id}", status_code=status.HTTP_204_NO_CONTENT)
async def delete_book_view(
    session: Annotated[AsyncSession, Depends(db_helper.session_getter)],
    book: Book = Depends(book_by_id),
) -> None:
    return await delete_book(
        session=session,
        book=book,
    )
