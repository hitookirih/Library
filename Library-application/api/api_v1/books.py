from typing import Annotated

from fastapi import APIRouter, Depends
from sqlalchemy.ext.asyncio import AsyncSession

from core.models import db_helper
from core.schemas.book import BookRead
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
