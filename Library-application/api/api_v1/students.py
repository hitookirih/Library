from typing import Annotated

from fastapi import APIRouter, Depends
from sqlalchemy.ext.asyncio import AsyncSession

from core.models import db_helper, Student
from core.schemas.student import StudentRead, StudentCreate
from crud import students as students_crud
from crud.students import student_by_id

router = APIRouter(tags=["Students"])


@router.get("", response_model=list[StudentRead])
async def get_students(
    session: Annotated[
        AsyncSession,
        Depends(db_helper.session_getter),
    ],
):
    students = await students_crud.get_all_students(session=session)
    return students


@router.get("{student_id}", response_model=StudentRead)
async def get_student_by_id(
    student: Student = Depends(student_by_id),
) -> Student:
    return student


@router.post("", response_model=StudentRead)
async def create_student(
    session: Annotated[
        AsyncSession,
        Depends(db_helper.session_getter),
    ],
    student_create: StudentCreate,
):
    student = await students_crud.create_student(
        session=session,
        student_create=student_create,
    )
    return student
