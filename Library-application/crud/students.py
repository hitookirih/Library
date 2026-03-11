from typing import Sequence

from sqlalchemy import select
from sqlalchemy.ext.asyncio import AsyncSession

from core.models import Student
from core.schemas.student import StudentCreate, StudentUpdatePartial, StudentUpdate


async def get_all_students(
    session: AsyncSession,
) -> Sequence[Student]:
    stmt = select(Student).order_by(Student.id)
    result = await session.scalars(stmt)
    return result.all()


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
