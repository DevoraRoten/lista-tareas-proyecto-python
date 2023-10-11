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
    print('tarea a agregar: ', tarea)
    sql = f"""
    INSERT INTO tareas (titulo, descripcion, fecha_vencimiento, estado)
    VALUES ('{tarea.titulo}', '{tarea.descripcion}', '{tarea.fecha_vencimiento}', '{tarea.estado}')
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
        print('base de datos no creada')
    
    return lista_tareas

def eliminar_tarea(id):
    conexion = ConexionBD()
    sql = f'DELETE FROM tareas WHERE id ={id}'
    try:
        conexion.cursor.execute(sql)
        conexion.cerrar()
    except:
        print('error al elimnar tarea')
    
def get_tarea_byid(id):
    conexion = ConexionBD()
    sql = f'SELECT * FROM tareas where id= {id}'
    tarea= ''
    try:
        conexion.cursor.execute(sql)
        tarea = conexion.cursor.fetchone()
        conexion.cerrar()
    except:
        print('error al buscar tarea')

    return tarea

def updated_tarea(tarea, id):
    conexion = ConexionBD()
    sql =f"""
    UPDATE tareas
    SET (titulo, descripcion, fecha_vencimiento, estado) 
    values ('{tarea.titulo}', '{tarea.descripcion}', '{tarea.fecha_vencimiento}', '{tarea.estado}')
    WHERE id={id}
    """
    try: 
        conexion.cursor.execute(sql)
        conexion.cerrar()
    except:
        print('error al actualizar')