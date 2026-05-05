from fastapi import FastAPI
from app.routers import router as tasks_router
from app.database import get_db
import uvicorn


conn = get_db()
conn.execute("CREATE TABLE IF NOT EXISTS tasks (id TEXT PRIMARY KEY, title TEXT, description TEXT)")

cursor = conn.execute("SELECT COUNT(*) FROM tasks")
if cursor.fetchone()[0] == 0:
    conn.execute("INSERT INTO tasks VALUES (?, ?, ?)", ("2", "Default Task 2", "Description 2"))
    conn.execute("INSERT INTO tasks VALUES (?, ?, ?)", ("4", "Default Task 4", "Description 4"))
    conn.commit()

conn.close()

app = FastAPI()
app.include_router(tasks_router)
if __name__ == '__main__':
    uvicorn.run(app)