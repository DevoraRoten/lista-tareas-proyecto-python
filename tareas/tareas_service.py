from BD.conexion_bd import ConexionBD
from models.tarea import TareaPost


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

def listar_tareas():
    conexion= ConexionBD()
    lista_tareas=[]
    sql = 'SELECT * FROM tareas'

    try:
        conexion.cursor.execute(sql)
        lista_tareas = conexion.cursor.fetchall()
        conexion.cerrar()
    except:
        lista_tareas='error al traer la lista de tareas'
    print(lista_tareas)
    return lista_tareas

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
        res = "No hay una tarea asociada al id {id} ingresado"
    else:
        sql = f'DELETE FROM tareas WHERE id ={id}'
        res=''
        try:
            conexion.cursor.execute(sql)
            conexion.cerrar()
            res= 'Tarea con id: {id} eliminada correctamente'
        except:
            res='error al elimnar tarea'
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
        tarea ='error al buscar tarea'
    if (tarea is None):
        tarea = "No hay una tarea asociada al id ingresado"
    return tarea

def updated_tarea(tarea, id):
    conexion = ConexionBD()
    resp= ''
    sql =f"""
    UPDATE tareas
    SET 
    titulo = '{tarea.titulo}', 
    descripcion = '{tarea.descripcion}', 
    fecha_vencimiento = '{tarea.fecha_vencimiento}', 
    estado = '{tarea.estado}'
    WHERE id={id}
    """
    try: 
        conexion.cursor.execute(sql)
        conexion.cerrar()
        resp ='tarea actualizada correctamente'
    except:
        resp = 'error al actualizar'
    return resp

def sumar(num1, num2):
    return num1+num2