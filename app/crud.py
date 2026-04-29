from app.schemas import TaskSchema

db = {
    
}

def get_tasks():
    return db

def add_task(id: str, task: TaskSchema):
    db[id] = task.dict()

def delete_tasks():
    db.clear()