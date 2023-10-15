Proyecto final para curso de python

############## como utilizar ###########

1- para levantar la api ejecute el siguiente comando en la terminal
uvicorn main:app --reload

2- para probar cada uno de los endpoint debe ocupar las siguientes URLs en postman con el metodo correspondiente:

    2.1 para obtener la lista de tareas quese encuentran en la base de datos use 
    GET -> http://localhost:8000/tareas 

    2.2 para obtener una de las tareas se puede obtenert por su ID en la siguiente URL ( donde el valor id de la tareas que es un valor numérico)
    GET -> http://localhost:8000/tareas/id

    2.3 para traer las tareas asociadas a un estado se debe utilizar el siguiente endpoint (donde 'estado' es un valor numerico entero)
    GET -> http://localhost:8000/filtros/estado

    2.4 para agregar una nueva tarea se debe utilizar el siguiente endpoint con el método POST
    POST -> http://localhost:8000/tareas 
    -> la tarea a agregar debe ennviarla por el body con formato JSON como se ve a continuacion:
    {
        "titulo": "string",
        "descripcion": "string",
        "fecha_vencimiento": "2023-10-15",
        "estado": 0
    }

    -donde el titulo y descripcion deben tener un valor string, "fecha_vencimiento" de tipo date y el estado debe ser un valor numerico

    2.5 para editar una tarea agregada se debe utilizar el método pu con el siguiente endpoint
    PUT -> http://localhost:8000/tareas/id
    -donde la 'id' corresponde a la id de la tarea que se desea editar
    - en el body se debe enbiar los nuevos datos de la tarea con el formato mostrado en el metodo post del punto 2.4

    2.6 para eliminar una tarea debemos utilizar el metodo delete con el siguiente endpoint
    DELETE -> http://localhost:8000/tareas/id
    -donde la id es la id de la tarea que se quier eliminar y es un número entero.

3. Para ejecutar las pruebas unitarias debemos ejecutar el siguiente comando en la consola: pytest

4. otros datos
-csrpeta models contiene las interfaces
-carpeta database es la base de datos utilizada
-carpeta tareas tiene un archivo 'tareas_service.py' con cada una de las funcionnes que se ejecutan en los métodos y 
    un archivo 'tareas_controller.py' con los endpoints de cada uno de los métodos y la ejecucion de cad uno de las funciones creadas en el servicio
-carpeta test contiene un archivo con pruebas asociadas a caa una de las funciones asociadas a los metodos

