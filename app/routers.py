from fastapi import APIRouter
from app import crud, schemas
router = APIRouter()

@router.get('/tasks')
def get_tasks():
    return crud.get_tasks()

@router.post('/tasks/{id}')
def create_task(id: str,task: schemas.TaskSchema):
    return crud.add_task(id=id,task=task)

@router.delete('/tasks')
def delete_tasks():
    return crud.delete_tasks()