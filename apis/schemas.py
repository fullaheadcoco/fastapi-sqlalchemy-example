from pydantic import BaseModel
from typing import Optional

class UserBase(BaseModel):
    data: Optional[dict] = None

class UserCreate(UserBase):
    pass

class User(UserBase):
    id: int

    class Config:
        orm_mode = True