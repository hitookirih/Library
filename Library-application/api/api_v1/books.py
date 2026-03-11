from typing import Annotated

from fastapi import APIRouter, Depends, status
from sqlalchemy.ext.asyncio import AsyncSession

from core.models import db_helper
from core.schemas.book import BookRead, BookCreate
from crud import books as books_crud

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
