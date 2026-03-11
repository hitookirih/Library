from fastapi import APIRouter

from core.config import settings

from .students import router as students_router

router = APIRouter(
    prefix=settings.api.v1.prefix,
)
router.include_router(
    students_router,
    prefix=settings.api.v1.students,
)
