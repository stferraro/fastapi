from pydantic import BaseModel

class Estudiante(BaseModel):
    nombre: str
    apellido: str
    cedula: str
    codigo_estudiante: str
    genero: str
    semestre_academico: str
    edad: int