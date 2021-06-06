from typing import List, Optional
from pydantic import BaseModel


class PostCreate(BaseModel):
    title: str
    description: Optional[str] = None


class UserBase(BaseModel):
    username: str
    email: str


class Post(PostCreate):
    id: int
    user_id: int
    user: UserBase

    class Config:
        orm_mode = True


class UserCreate(UserBase):
    password: str


class User(UserBase):
    id: int
    posts: List[Post] = []

    class Config:
        orm_mode = True
