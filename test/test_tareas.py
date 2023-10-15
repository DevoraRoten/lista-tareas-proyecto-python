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
        "estado": 2
    }
    arreglo = guardar_tarea(tarea)
    assert len(arreglo) > 0

## traer la lista de tareas, que solo debe haber una porque al principio de las pruebas eliminamos la tabla y solo hemos agragado una tarea
def test_listar_tareas():
    arr = listar_tareas()
    assert len(arr) > 0
    assert len(arr) == 1
    assert arr[0][1] == 'tarea test'


# agregar una nueva tarea
def test_guardar_otra_tarea():
    tarea: TareaPost = {
        "titulo": 'segunda tarea test',
        "descripcion": 'tarea creada para un test unitario',
        "fecha_vencimiento": '20 de enero',
        "estado": 3
    }
    arreglo = guardar_tarea(tarea)
    assert len(arreglo) > 0
    assert len (arreglo) == 2

# traer una tarea por su id
def test_get_tarea_id():
    tarea = get_tarea_byid(1) 
    assert tarea != None
    assert tarea != "No hay una tarea asociada al id ingresado"

## actualizar segunda tarea agreagada
def test_actualizar_tarea():
    tarea: TareaPost = {
        "titulo": 'segunda tarea test editada',
        "descripcion": 'tarea creada para un test unitario',
        "fecha_vencimiento": '20 de enero',
        "estado": 4
    }
    assert updated_tarea(tarea, 2) =='tarea actualizada correctamente'

## traer la lista de tareas, que solo debe haber una porque al principio de las pruebas eliminamos la tabla y solo hemos agragado una tarea
def test_listar_tareas_2():
    arr = listar_tareas()
    assert len(arr) > 0
    assert len(arr) == 2
    assert arr[1][1] == 'segunda tarea test editada'

def traer_tareas_por_estado():
    tareas = get_tarea_by_estado(4)
    assert len(tareas)==1
    assert tareas[0][0]==2

def traer_tareas_por_estado_2():
    tareas = get_tarea_by_estado(2)
    assert len(tareas)==1
    assert tareas[0][0]==1


### eliminar la tarea con id 2
def test_eliminar_tarea():
    assert eliminar_tarea(2) == 'Tarea con id: 2 eliminada correctamente'

## eliminar tarea ya eliminada
def test_eliminar_tarea_eliminada():
    assert eliminar_tarea(2) == 'No hay una tarea asociada al id 2 ingresado'

## traer la lista de tareas, que solo debe haber una porque al principio de las pruebas eliminamos la tabla y solo hemos agragado una tarea
def test_listar_tareas_3():
    arr = listar_tareas()
    assert len(arr) > 0
    assert len(arr) == 1
