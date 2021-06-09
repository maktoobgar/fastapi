from typing import List
from fastapi import APIRouter, Depends, status, HTTPException
from app import schemas, database, models, oauth2
from sqlalchemy.orm import Session
from app.repository import post, user

router_posts = APIRouter(
    prefix="/posts",
    tags=['Posts']
)

get_db = database.get_db


@router_posts.post('/', status_code=status.HTTP_201_CREATED)
def create(request: schemas.Post, db: Session = Depends(get_db), current_user: schemas.User = Depends(oauth2.get_current_user)):
    current_user = user.show_with_username(current_user.email, db)
    return post.create(request, db, current_user)


router = APIRouter(
    prefix="/post",
    tags=['Post']
)

@router.delete('/{id}', status_code=status.HTTP_204_NO_CONTENT)
def destroy(id: int, db: Session = Depends(get_db), current_user: schemas.User = Depends(oauth2.get_current_user)):
    return post.destroy(id, db)


@router.get('/{id}', status_code=200)
def show(id: int, db: Session = Depends(get_db), current_user: schemas.User = Depends(oauth2.get_current_user)):
    return post.show(id, db)
