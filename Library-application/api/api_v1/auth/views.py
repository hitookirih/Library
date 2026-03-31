from fastapi import APIRouter

from core.config import settings
from jwt_auth import router as jwt_auth_router

router = APIRouter(
    prefix=settings.api.v1.prefix,
)

router.include_router(
    jwt_auth_router,
    prefix=settings.api.v1.auth,
)
