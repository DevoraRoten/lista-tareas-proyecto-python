from fastapi import FastAPI
from models.tarea import Tarea

app = FastAPI()

tareas = [
    {
        "id": 1,
        "titulo": "tarea 1",
        "descripcion": "desarrollr metodo get para las tareas creadas",
        "fecha_vencimiento": "1 de Septiembre de 2023",
        "estado": 1
    },
      {
        "id": 2,
        "titulo": "tarea 2",
        "descripcion": "desarrollr metodo post para crear una nueva tarea", 
        "fecha_vencimiento": "20 de Septiembre de 2023",
        "estado": 1
    }
]

@app.get('/tareas')
def get_tareas():
    return tareas

@app.get('/tareas/{id}')
def get_tarea(id: int):
    return list(filter(lambda item: item['id']==id, tareas))