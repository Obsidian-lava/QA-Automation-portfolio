from fastapi import FastAPI
from app.routers import router as tasks_router
import uvicorn

app = FastAPI()
app.include_router(tasks_router)
if __name__ == '__main__':
    uvicorn.run(app)