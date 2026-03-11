from typing import Sequence

from sqlalchemy import select
from sqlalchemy.ext.asyncio import AsyncSession

from core.models import Student
from core.schemas.student import StudentCreate


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
