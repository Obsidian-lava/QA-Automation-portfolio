from fastapi import APIRouter
from app import crud, schemas
router = APIRouter()

@router.get('/tasks')
def get_tasks():
    return crud.get_tasks()

@router.post('/tasks/{id}')
def create_task(id: str,task: schemas.TaskSchema):
    return crud.add_task(id=id,task=task)

@router.delete('/tasks/{id}')
def delete_tasks(id):
    return crud.delete_tasks(id)

@router.put('/tasks/{id}')
def edit_task(id, task: schemas.TaskSchema):
    existing_tasks = get_tasks()

    if id not in existing_tasks:
        return {"error": "Task not found"}, 404

    return crud.update_task(id, task.title, task.description)