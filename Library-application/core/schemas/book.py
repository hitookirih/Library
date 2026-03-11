from pydantic import BaseModel


class BookBase(BaseModel):

    title: str
    author: str
    description: str

    cover: str


class BookCreate(BookBase):
    pass


class BookRead(BookBase):
    id: int
