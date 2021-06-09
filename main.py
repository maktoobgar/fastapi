from fastapi import FastAPI
from app import  models
from app.database import engine
from app.routers import post, authentication

app = FastAPI()

models.Base.metadata.create_all(engine)

app.include_router(authentication.router)
app.include_router(post.router)
app.include_router(post.router_posts)
