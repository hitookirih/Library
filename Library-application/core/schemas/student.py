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


class StudentRead(StudentBase):
    id: int
