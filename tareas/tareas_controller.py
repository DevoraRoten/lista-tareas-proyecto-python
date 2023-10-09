from fastapi import APIRouter
from models.tarea import Tarea
from models.tarea import TareaPost

tareas = APIRouter()

array_tareas = [
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

@tareas.get('/')
def saludo():
    return 'holi'

@tareas.get('/tareas')
def get_tareas():
    return array_tareas

@tareas.get('/tareas/{id}')
def get_tarea(id: int):
    return list(filter(lambda item: item['id']==id, array_tareas))

@tareas.post('/tareas')
def post_tareas(tarea: Tarea):
    array_tareas.append(tarea)
    return array_tareas

@tareas.put('/tareas/{id}')
def update_tarea(id: int, tarea: TareaPost):
    for index, item in enumerate(array_tareas):
        if item['id'] == id :
            array_tareas[index]['titulo'] = tarea.titulo
            array_tareas[index]['descripcion'] = tarea.descripcion
            array_tareas[index]['fecha_vencimiento'] = tarea.fecha_vencimiento
            array_tareas[index]['estado'] = tarea.estado
    return array_tareas

@tareas.delete('/tareas{id}')
def delete_tarea(id:int):
    return list(filter(lambda item: item['id']==id, array_tareas))