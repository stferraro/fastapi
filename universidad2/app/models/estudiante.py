# coding: utf-8

from sqlmodel import SQLModel, Field
from typing import Optional

class Estudiante(SQLModel, table=True):
    id: Optional[int] = Field(default=None, primary_key=True)
    nombre: str
    apellido: str
    edad: int
    correo: str
    genero: str 
    codigo_estudiante: str = Field(unique=True, index=True)
