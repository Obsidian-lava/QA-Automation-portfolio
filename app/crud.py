from app.schemas import TaskSchema

db = {
    "2": {"title": "...",
          "description": "..."},
    "4": {"title": "...",
          "description": "..."}
}

def get_tasks():
    return db

def add_task(id: str, task: TaskSchema):
    db[id] = task.dict()

def delete_tasks(id: str):
    if id in db:
        del db[id]
        return {"message": f"Task {id} deleted"}
    return {"error": "task not found"}, 404