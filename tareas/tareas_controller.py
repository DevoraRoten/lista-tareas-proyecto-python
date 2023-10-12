from fastapi import APIRouter
from models.tarea import Tarea
from models.tarea import TareaPost
from BD.funciones_BD import crear_tabla, borrar_tabla, guardar_tarea, listar_tareas, eliminar_tarea, get_tarea_byid, updated_tarea
#import tkinter as tk

tareas = APIRouter()


#def menu_tareas():
#    root = tk.Tk()
#    root.title('hola')
#    root.mainloop()


#if __name__ == '__menu_tareas__':
#    menu_tareas()

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
