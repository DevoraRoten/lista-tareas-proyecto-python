from fastapi import APIRouter
from models.tarea import Tarea
from models.tarea import TareaPost
from tareas.tareas_service import crear_tabla, borrar_tabla, guardar_tarea, listar_tareas, eliminar_tarea, get_tarea_byid, updated_tarea

tareas = APIRouter()

@tareas.get('/')
def saludo():
    crear_tabla()
    return 'holi'


@tareas.get('/tareas')
def get_tareas():
    return listar_tareas()


@tareas.get('/tareas/{id}')
def get_tarea(id: int):
    return get_tarea_byid(id)


@tareas.post('/tareas')
def post_tareas(tarea: TareaPost):
    return guardar_tarea(tarea)


@tareas.put('/tareas/{id}')
def update_tarea(id: int, tarea: TareaPost):
    return updated_tarea(tarea, id)


@tareas.delete('/tareas{id}')
def delete_tarea(id: int):
    return eliminar_tarea(id)
