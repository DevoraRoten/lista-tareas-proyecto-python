from fastapi import APIRouter
from models.tarea import Tarea
from models.tarea import TareaPost
from BD.funciones_BD import crear_tabla, borrar_tabla, guardar_tarea, listar_tareas, eliminar_tarea
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
    return list(filter(lambda item: item['id'] == id, array_tareas))


@tareas.post('/tareas')
def post_tareas(tarea: TareaPost):
    guardar_tarea(tarea)
    array_tareas.append(tarea)
    return array_tareas


@tareas.put('/tareas/{id}')
def update_tarea(id: int, tarea: TareaPost):
    for index, item in enumerate(array_tareas):
        if item['id'] == id:
            array_tareas[index]['titulo'] = tarea.titulo
            array_tareas[index]['descripcion'] = tarea.descripcion
            array_tareas[index]['fecha_vencimiento'] = tarea.fecha_vencimiento
            array_tareas[index]['estado'] = tarea.estado
    return array_tareas


@tareas.delete('/tareas{id}')
def delete_tarea(id: int):
    eliminar_tarea(id)
    return 'tarea eliminadda'
