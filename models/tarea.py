from pydantic import BaseModel

class Tarea(BaseModel):
    id: int
    titulo: str
    descripcion: str
    fecha_vencimiento: str
    estado: int