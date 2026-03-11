from typing import Sequence, Annotated

from fastapi import Path, HTTPException, status, Depends
from sqlalchemy import select
from sqlalchemy.ext.asyncio import AsyncSession

from core.models import Student, db_helper
from core.schemas.student import (
    StudentCreate,
    StudentUpdatePartial,
    StudentUpdate,
    StudentRead,
)


async def get_student(session: AsyncSession, student_id: int) -> Student | None:
    return await session.get(Student, student_id)


async def get_all_students(
    session: AsyncSession,
) -> Sequence[Student]:
    stmt = select(Student).order_by(Student.id)
    result = await session.scalars(stmt)
    return result.all()


async def student_by_id(
    student_id: Annotated[int, Path],
    session: AsyncSession = Depends(db_helper.session_getter),
) -> Student | None:
    student = await get_student(session=session, student_id=student_id)
    if student is not None:
        return student
    raise HTTPException(
        status_code=status.HTTP_404_NOT_FOUND, detail=f"Student {student_id} not found!"
    )


async def create_student(
    session: AsyncSession,
    student_create: StudentCreate,
) -> Student:
    student = Student(**student_create.model_dump())
    session.add(student)
    await session.commit()
    await session.refresh(student)
    return student


async def update_student(
    session: AsyncSession,
    student: Student,
    student_update: StudentUpdate | StudentUpdatePartial,
    partial: bool = False,
) -> Student:
    for name, value in student_update.model_dump(exclude_unset=partial).items():
        setattr(student, name, value)
        await session.commit()
    return student


async def delete_student(session: AsyncSession, student: Student) -> None:
    await session.delete(student)
    await session.commit()
