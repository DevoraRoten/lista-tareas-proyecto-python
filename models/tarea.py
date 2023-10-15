from pydantic import BaseModel
from datetime import date

class Tarea(BaseModel):
    id: int
    titulo: str
    descripcion: str
    fecha_vencimiento: date
    estado: int

class TareaPost(BaseModel):
    titulo: str
    descripcion: str
    fecha_vencimiento: date
    estado: int