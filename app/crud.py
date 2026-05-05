from app.schemas import TaskSchema
from app.database import get_db

db = {
    "2": {"title": "...",
          "description": "..."},
    "4": {"title": "...",
          "description": "..."}
}

def get_tasks():
    conn = get_db()

    cursor = conn.execute("SELECT * FROM tasks")
    rows = cursor.fetchall()

    conn.close()
    return {row['id']: {"title": row['title'], "description": row['description']} for row in rows}

def add_task(id: str, task: TaskSchema):
    conn = get_db()

    conn.execute(
        "INSERT INTO tasks (id, title, description) VALUES (?, ?, ?)",
        (id, task.title, task.description))
    conn.commit()
    conn.close()

def delete_tasks(id: str):
    conn = get_db()

    cur = conn.execute("SELECT id FROM tasks WHERE id = ?", (id,))
    if cur.fetchone():
        conn.execute("DELETE FROM tasks WHERE id = ?", (id,))
        conn.commit()
        conn.close()
        return {"message": f"Task {id} deleted"}
    conn.close()
    return {"error": "task not found"}, 404