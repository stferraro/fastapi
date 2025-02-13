from fastapi import APIRouter, HTTPException, Request
from fastapi.responses import HTMLResponse
from fastapi.templating import Jinja2Templates
from app.models import Estudiante
import json
import os

router = APIRouter()
templates = Jinja2Templates(directory="app/templates")

DATA_FILE = "app/data/estudiantes.json"

def load_data():
    if not os.path.exists(DATA_FILE):
        with open(DATA_FILE, "w") as file:
            json.dump([], file)
    with open(DATA_FILE, "r") as file:
        return json.load(file)

def save_data(data):
    with open(DATA_FILE, "w") as file:
        json.dump(data, file, indent=4)

@router.get("/", response_class=HTMLResponse)
async def read_estudiantes(request: Request):
    estudiantes = load_data()
    return templates.TemplateResponse("index.html", {"request": request, "estudiantes": estudiantes})

@router.get("/crear", response_class=HTMLResponse)
async def crear_estudiante_form(request: Request):
    return templates.TemplateResponse("crear_estudiante.html", {"request": request})

@router.post("/crear")
async def crear_estudiante(estudiante: Estudiante):
    data = load_data()
    data.append(estudiante.model_dump())
    save_data(data)
    return {"message": "Estudiante creado exitosamente"}

@router.get("/buscar")
async def buscar_estudiante(request: Request, codigo_estudiante: str):
    estudiantes = load_data()
    estudiante = next((e for e in estudiantes if e["codigo_estudiante"] == codigo_estudiante), None)
    if estudiante:
        return templates.TemplateResponse("buscar_estudiante.html", {"request": request, "estudiante": estudiante})
    else:
        raise HTTPException(status_code=404, detail="Estudiante no encontrado")
