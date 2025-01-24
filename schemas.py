from typing import Any, List, Union

import peewee
from pydantic import BaseModel
from pydantic.utils import GetterDict

class PeeweeGetterDict(GetterDict):
    def get(self, key: Any, default: Any = None):
        res = getattr(self._obj, key, default)
        if isinstance(res, peewee.ModelSelect):
            return list(res)
        return res


class ActorBase(BaseModel):
    name: str
    surname: str

class Actor(ActorBase):
    id: int

class MovieBase(BaseModel):
    title: str
    year: int
    director: str
    description: Union[str, None] = None

class MovieCreate(MovieBase):
    pass


class Movie(MovieBase):
    id: int
    actors: List[Actor] = []

    class Config:
        orm_mode = True
        getter_dict = PeeweeGetterDict
