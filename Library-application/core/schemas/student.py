from pydantic import BaseModel


class StudentBase(BaseModel):
    number_of_studak: int
    number_of_group: str
    name: str
    surname: str
    father_name: str
    phone_number: int
    telegram_id: str
    status: str


class StudentCreate(StudentBase):
    pass


class StudentUpdate(StudentCreate):
    pass


class StudentUpdatePartial(StudentCreate):
    number_of_studak: int | None = None
    number_of_group: str | None = None
    name: str | None = None
    surname: str | None = None
    father_name: str | None = None
    phone_number: int | None = None
    telegram_id: str | None = None
    status: str | None = None


class StudentRead(StudentBase):
    id: int
