from typing import List, Optional
from pydantic import BaseModel


class PostBase(BaseModel):
    title: str
    context: str


class Post(PostBase):

    class Config():
        orm_mode = True


class User(BaseModel):
    id: int
    username: str
    email: str
    password: str


class ShowPost(BaseModel):
    id: int
    title: str
    body: str
    creator: User

    class Config():
        orm_mode = True


class ShowUser(BaseModel):
    id: int
    username: str
    email: str
    posts: List[ShowPost] = []

    class Config():
        orm_mode = True


class Login(BaseModel):
    username: str
    password: str


class Token(BaseModel):
    access_token: str
    token_type: str


class TokenData(BaseModel):
    email: Optional[str] = None
