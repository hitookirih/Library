from pydantic import BaseModel


class BookBase(BaseModel):
    title: str
    author: str
    description: str | None = None


class BookCreate(BookBase):
    pass


class BookUpdate(BookBase):
    pass


class BookRead(BookBase):
    id: int


class BookUpdatePartial(BookBase):
    title: str | None = None
    author: str | None = None
    description: str | None = None
