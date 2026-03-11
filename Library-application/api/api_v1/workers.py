from typing import Annotated

from fastapi import APIRouter, Depends, status
from sqlalchemy.ext.asyncio import AsyncSession

from core.models import db_helper, Worker
from core.schemas.worker import WorkerRead, WorkerCreate, WorkerUpdate
from crud import workers as workers_crud
from crud.workers import worker_by_id, update_worker, delete_worker

router = APIRouter(tags=["Workers"])


@router.get("", response_model=list[WorkerRead])
async def get_workers(
    session: Annotated[
        AsyncSession,
        Depends(db_helper.session_getter),
    ],
):
    workers = await workers_crud.get_all_workers(session=session)
    return workers


@router.get("{worker_id}", response_model=WorkerRead)
async def get_worker_by_id(
    worker: Worker = Depends(worker_by_id),
) -> Worker:
    return worker


@router.post("", response_model=WorkerRead, status_code=status.HTTP_201_CREATED)
async def create_worker(
    session: Annotated[
        AsyncSession,
        Depends(db_helper.session_getter),
    ],
    worker_create: WorkerCreate,
):
    worker = await workers_crud.create_worker(
        session=session,
        worker_create=worker_create,
    )
    return worker


@router.put("{worker_id}", response_model=WorkerRead)
async def view_worker_update(
    session: Annotated[AsyncSession, Depends(db_helper.session_getter)],
    worker_update: WorkerUpdate,
    worker: Worker = Depends(worker_by_id),
) -> Worker:
    return await update_worker(
        session=session,
        worker=worker,
        worker_update=worker_update,
    )


@router.patch("{worker_id}", response_model=WorkerRead)
async def view_worker_update(
    session: Annotated[AsyncSession, Depends(db_helper.session_getter)],
    worker_update: WorkerUpdate,
    worker: Worker = Depends(worker_by_id),
) -> Worker:
    return await update_worker(
        session=session, worker=worker, worker_update=worker_update, partial=True
    )


@router.delete("{worker_id}", status_code=status.HTTP_204_NO_CONTENT)
async def delete_worker_view(
    session: Annotated[AsyncSession, Depends(db_helper.session_getter)],
    worker: Worker = Depends(worker_by_id),
) -> None:
    return await delete_worker(
        session=session,
        worker=worker,
    )
