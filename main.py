from typing import Optional
from fastapi import Body, FastAPI
from pydantic import BaseModel

app = FastAPI()

class Post(BaseModel):
    title: str 
    content: str 
    published: bool = True 
    rating: Optional[int] = None


@app.get("/")
def root():
    
    return {"Name": "Connor"}

@app.get("/posts")
def get_posts():
    return {"data": "This is a post"}

@app.post("/createposts")
def create_posts(post: Post):
    print(post)
    return {"data": "new post"}

# title str, content str, category, bool published or draft


