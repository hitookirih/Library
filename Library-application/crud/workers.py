from typing import Sequence, Annotated

from fastapi import Path, HTTPException, status, Depends
from sqlalchemy import select
from sqlalchemy.ext.asyncio import AsyncSession

from core.models import Worker, db_helper
from core.schemas.worker import WorkerCreate, WorkerUpdate, WorkerUpdatePartial


async def get_worker(session: AsyncSession, worker_id: int) -> Worker | None:
    return await session.get(Worker, worker_id)


async def get_all_workers(
    session: AsyncSession,
) -> Sequence[Worker]:
    stmt = select(Worker).order_by(Worker.id)
    result = await session.scalars(stmt)
    return result.all()


async def worker_by_id(
    worker_id: Annotated[int, Path],
    session: AsyncSession = Depends(db_helper.session_getter),
) -> Worker | None:
    worker = await get_worker(session=session, worker_id=worker_id)
    if worker is not None:
        return worker
    raise HTTPException(
        status_code=status.HTTP_404_NOT_FOUND, detail=f"Worker {worker_id} not found!"
    )


async def create_worker(
    session: AsyncSession,
    worker_create: WorkerCreate,
) -> Worker:
    worker = Worker(**worker_create.model_dump())
    session.add(worker)
    await session.commit()
    await session.refresh(worker)
    return worker


async def update_worker(
    session: AsyncSession,
    worker: Worker,
    worker_update: WorkerUpdate | WorkerUpdatePartial,
    partial: bool = False,
) -> Worker:
    for name, value in worker_update.model_dump(exclude_unset=partial).items():
        setattr(worker, name, value)
        await session.commit()
    return worker


async def delete_worker(session: AsyncSession, worker: Worker) -> None:
    await session.delete(worker)
    await session.commit()
