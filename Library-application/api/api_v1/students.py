from typing import Annotated

from fastapi import APIRouter, Depends, status
from sqlalchemy.ext.asyncio import AsyncSession

from core.models import db_helper, Student
from core.schemas.student import (
    StudentRead,
    StudentCreate,
    StudentUpdate,
    StudentUpdatePartial,
)
from crud import students as students_crud
from crud.students import student_by_id, update_student, delete_student

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


@router.post("", response_model=StudentRead, status_code=status.HTTP_201_CREATED)
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


@router.put("{student_id}", response_model=StudentRead)
async def view_student_update(
    session: Annotated[AsyncSession, Depends(db_helper.session_getter)],
    student_update: StudentUpdate,
    student: Student = Depends(student_by_id),
) -> Student:
    return await update_student(
        session=session,
        student=student,
        student_update=student_update,
    )


@router.patch("{student_id}", response_model=StudentRead)
async def view_student_update_partial(
    session: Annotated[AsyncSession, Depends(db_helper.session_getter)],
    student_update: StudentUpdatePartial,
    student: Student = Depends(student_by_id),
) -> Student:
    return await update_student(
        session=session,
        student=student,
        student_update=student_update,
        partial=True,
    )


@router.delete("{student_id}", status_code=status.HTTP_204_NO_CONTENT)
async def delete_student_view(
    session: Annotated[AsyncSession, Depends(db_helper.session_getter)],
    student: Student = Depends(student_by_id),
) -> None:
    return await delete_student(
        session=session,
        student=student,
    )
