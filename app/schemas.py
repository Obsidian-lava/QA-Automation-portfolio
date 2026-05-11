from pydantic import BaseModel
from typing import Optional

class TaskSchema(BaseModel):
    title: str
    description: str

class TaskUpdateSchema(BaseModel):
    title: Optional[str] = None
    description: Optional[str] = None