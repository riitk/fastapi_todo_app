from pydantic import BaseModel
from typing import Optional

class Todo(BaseModel):
    id: Optional[int] = None
    title: str
    description: Optional[str] = None
    completed: bool= False

class User(BaseModel):
    email : str
    password: str
