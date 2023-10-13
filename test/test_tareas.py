from tareas.tareas_service import *
from models.tarea import TareaPost


## eliminar tabla y crear tabla
def test_setUp():
    borrar_tabla()
    crear_tabla()

## guardar una tarea y comprobar que hay una tarea en la base de datos
def test_guardar_tarea():
    tarea: TareaPost = {
        "titulo": 'tarea test',
        "descripcion": 'tarea creada para un test unitario',
        "fecha_vencimiento": '15 de enero',
        "estado": 1
    }
    arreglo = guardar_tarea(tarea)
    assert len(arreglo) > 0

## traer la lista de tareas, que solo debe haber una porque al principio de las pruebas eliminamos la tabla y solo hemos agragado una tarea
def test_listar_tareas():
    arr = listar_tareas()
    assert len(arr) > 0
    assert len(arr) == 1
    assert arr[0][1] == 'tarea test'





