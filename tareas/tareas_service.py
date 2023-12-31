from BD.conexion_bd import ConexionBD
from models.tarea import TareaPost, Tarea
from fastapi import HTTPException


def crear_tabla():
    conexion = ConexionBD()

    sql = '''
    CREATE TABLE  tareas(
        id INTEGER,
        titulo VARCHAR(100),
        descripcion VARCHAR,
        fecha_vencimiento VARCHAR,
        estado INTEGER,
        PRIMARY KEY(id AUTOINCREMENT)
    )
    '''
    conexion.cursor.execute(sql)
    conexion.cerrar()

## agregar una tarea
def borrar_tabla():
    conexion = ConexionBD()
    sql = 'DROP TABLE tareas'
    conexion.cursor.execute(sql)
    conexion.cerrar()


def guardar_tarea(tarea):
    conexion = ConexionBD()
    try:
        titulo= tarea['titulo']
        descripcion= tarea['descripcion']
        fecha_vencimiento= tarea['fecha_vencimiento']
        estado= tarea['estado']
    except:
        titulo=tarea.titulo
        descripcion= tarea.descripcion
        fecha_vencimiento=tarea.fecha_vencimiento
        estado=tarea.estado
    sql = f"""
    INSERT INTO tareas (titulo, descripcion, fecha_vencimiento, estado)
    VALUES ('{titulo}', '{descripcion}', '{fecha_vencimiento}', '{estado}')
    """
    sql_data= 'SELECT * FROM tareas'
    tareas=[]
    try:
        conexion.cursor.execute(sql)
        conexion.cursor.execute(sql_data)
        tareas = conexion.cursor.fetchall()
        conexion.cerrar()
    except:
        print('error al agregar')
    return tareas

## listar todas las tareas de la base de datos
def listar_tareas():
    conexion= ConexionBD()
    lista_tareas=[]
    sql = 'SELECT * FROM tareas'

    try:
        conexion.cursor.execute(sql)
        lista_tareas = conexion.cursor.fetchall()
        conexion.cerrar()
    except:
        raise HTTPException(status_code=400, detail='error al traer la lista de tareas')
    return lista_tareas

#eliminar una tarea
def eliminar_tarea(id):
    conexion = ConexionBD()
    
    sql = f'SELECT * FROM tareas where id= {id}'
    tarea= ''
    try:
        conexion.cursor.execute(sql)
        tarea = conexion.cursor.fetchone()
        conexion.cerrar()
    except:
        tarea ='error al buscar tarea'
    if (tarea is None):
        raise HTTPException(status_code=404, detail=f'No hay una tarea asociada al id {id} ingresado')
    else:
        sql = f"""DELETE FROM tareas WHERE id= {id} """ 
        res=''
        try:
            conexion = ConexionBD()
            conexion.cursor.execute(sql)
            conexion.cerrar()
            res= f'Tarea con id: {id} eliminada correctamente'
        except:
            raise HTTPException(status_code=400, detail='error al eliminar tarea')
    return res
    
def get_tarea_byid(id):
    conexion = ConexionBD()
    sql = f'SELECT * FROM tareas where id= {id}'
    tarea= ''
    try:
        conexion.cursor.execute(sql)
        tarea = conexion.cursor.fetchone()
        conexion.cerrar()
    except:
         raise HTTPException(status_code=400, detail='error al buscar tarea')
    if (tarea is None):
        raise HTTPException(status_code=404, detail=f'No hay una tarea asociada al id {id} ingresado')
    return tarea

def updated_tarea(tarea, id):
    get_tarea_byid(id)
    conexion = ConexionBD()
    try:
        titulo= tarea['titulo']
        descripcion= tarea['descripcion']
        fecha_vencimiento= tarea['fecha_vencimiento']
        estado= tarea['estado']
    except:
        titulo=tarea.titulo
        descripcion= tarea.descripcion
        fecha_vencimiento=tarea.fecha_vencimiento
        estado=tarea.estado
    resp= ''
    sql =f"""
    UPDATE tareas
    SET 
    titulo = '{titulo}',
    descripcion = '{descripcion}', 
    fecha_vencimiento = '{fecha_vencimiento}', 
    estado = '{estado}'
    WHERE id={id}
    """
    try: 
        conexion.cursor.execute(sql)
        conexion.cerrar()
        resp ='tarea actualizada correctamente'
    except:
        raise HTTPException(status_code=400, detail=f'error al actualizar la tarea')
    return resp

def get_tarea_by_estado(estado):
    conexion = ConexionBD()
    sql = f'SELECT * FROM tareas where estado= {estado}'
    tarea= ''
    try:
        conexion.cursor.execute(sql)
        tarea = conexion.cursor.fetchall()
        conexion.cerrar()
    except:
         raise HTTPException(status_code=400, detail=f'error al buscar tarea por estado')
    if (len(tarea)==0):
        raise HTTPException(status_code=404, detail=f'No hay una tarea asociada al estado ingresado')
    return tarea


def cambiarFormato(tareas):
    auxTareas=[]
    for tarea in tareas:
        aux={
            "id": tarea[0],
            "titulo": tarea[1],
            "descripcion": tarea[2],
            "fecha_vencimiento": tarea[3],
            "estado": tarea[4]
        }
        auxTareas.append(aux)
    return auxTareas

def cambiarFormatoOne(tarea):
    aux= {
         "id": tarea[0],
         "titulo": tarea[1],
         "descripcion": tarea[2],
         "fecha_vencimiento": tarea[3],
         "estado": tarea[4]
    }
    return aux
