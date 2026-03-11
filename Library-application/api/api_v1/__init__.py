from fastapi import APIRouter

from core.config import settings

from .students import router as students_router
from .books import router as books_router

router = APIRouter(
    prefix=settings.api.v1.prefix,
)
router.include_router(
    students_router,
    prefix=settings.api.v1.students,
)

router.include_router(
    books_router,
    prefix=settings.api.v1.books,
)
