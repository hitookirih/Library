from pydantic import BaseModel


class WorkerBase(BaseModel):

    fullname: str
    phone_number: int
    telegram_id: int
    status: str


class WorkerCreate(WorkerBase):
    pass


class WorkerUpdate(WorkerBase):
    pass


class WorkerRead(WorkerBase):
    id: int


class WorkerUpdatePartial(WorkerBase):

    fullname: str | None = None
    phone_number: int | None = None
    telegram_id: int | None = None
    status: str | None = None
