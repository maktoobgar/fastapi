from fastapi import FastAPI
from typing import Optional
from pydantic import BaseModel
import uvicorn

app = FastAPI()


class Post(BaseModel):
    title: str
    context: str

class PostUpdate(BaseModel):
    title: Optional[str]
    context: Optional[str]

# region /posts
@app.get('/posts')
def show_posts():
    return [
        {'title': 'some title', 'context': 'some context'},
        {'title': 'some title', 'context': 'some context'},
        {'title': 'some title', 'context': 'some context'}
    ]

@app.post('/posts', status_code=201)
def create_post(body: Post):
    return {'title': 'new title', 'context': 'new context'}
# endregion

# region /post/{id}
@app.get('/post/{id}')
def show_post(id: int):
    return {'id': 1, 'title': 'new title', 'context': 'new context'}

@app.route('/post/{id}', ['PUT', 'PATCH'])
def update_post(body: PostUpdate, id: int):
    # 202: accepted
    return {'id': id, 'title': 'new title', 'context': 'new context'}

@app.delete('/post/{id}', status_code=204)
def delete_post(id: int):
    return

# endregion

@app.get('/',)
def index():
    return {'message': 'hello world'}


if __name__ == "__main__":
    uvicorn.run(app, host='127.0.0.1', port=3333)