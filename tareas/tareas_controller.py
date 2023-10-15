from fastapi import APIRouter
from models.tarea import Tarea
from models.tarea import TareaPost
from tareas.tareas_service import crear_tabla, borrar_tabla, guardar_tarea, listar_tareas, eliminar_tarea, get_tarea_byid, updated_tarea, get_tarea_by_estado, cambiarFormato, cambiarFormatoOne

tareas = APIRouter()


@tareas.get('/tareas')
def get_tareas():
    return cambiarFormato(listar_tareas())


@tareas.get('/tareas/{id}')
def get_tarea(id: int):
    return cambiarFormatoOne(get_tarea_byid(id))

@tareas.get('/filtro/{estado}')
def get_tarea_filtro(estado: int):
    return cambiarFormato(get_tarea_by_estado(estado))

@tareas.post('/tareas')
def post_tareas(tarea: TareaPost):
    return cambiarFormato(guardar_tarea(tarea))


@tareas.put('/tareas/{id}')
def update_tarea(id: int, tarea: TareaPost):
    return updated_tarea(tarea, id)


@tareas.delete('/tareas/{id}')
def delete_tarea(id: int):
    return eliminar_tarea(id)