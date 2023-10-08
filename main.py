from fastapi import FastAPI
from tareas.tareas_controller import tareas

app = FastAPI()
app.include_router(tareas)