from fastapi import APIRouter, Depends, HTTPException, Request, Form
from sqlmodel import Session, select
from fastapi.templating import Jinja2Templates
from app.database.connection import db
from app.models.estudiante import Estudiante

router = APIRouter(prefix="/estudiantes", tags=["Estudiantes"])
templates = Jinja2Templates(directory="app/templates")

# Dependencia para obtener sesión de BD
def get_session():
    with Session(db.engine) as session:
        yield session

# Ruta para listar estudiantes
@router.get("/")
def listar_estudiantes(request: Request, session: Session = Depends(get_session)):
    estudiantes = session.exec(select(Estudiante)).all()
    return templates.TemplateResponse("estudiante/listar.html", {"request": request, "estudiantes": estudiantes})

# Ruta para mostrar formulario de agregar estudiante
@router.get("/agregar")
def mostrar_formulario_agregar(request: Request):
    return templates.TemplateResponse("estudiante/agregar.html", {"request": request})

# Ruta para procesar agregar estudiante
@router.post("/agregar")
def agregar_estudiante(
    request: Request,
    nombre: str = Form(...),
    apellido: str = Form(...),
    edad: int = Form(...),
    correo: str = Form(...),
    genero: str = Form(...),
    codigo_estudiante: str = Form(...),
    session: Session = Depends(get_session)
):
    nuevo_estudiante = Estudiante(
        nombre=nombre,
        apellido=apellido,
        edad=edad,
        correo=correo,
        genero=genero,
        codigo_estudiante=codigo_estudiante
    )

    session.add(nuevo_estudiante)
    session.commit()
    session.refresh(nuevo_estudiante)

    return templates.TemplateResponse("estudiante/agregar.html", {"request": request, "mensaje": "Estudiante agregado exitosamente"})

# Ruta para mostrar formulario de edición
@router.get("/editar/{estudiante_id}")
def mostrar_formulario_editar(request: Request, estudiante_id: int, session: Session = Depends(get_session)):
    estudiante = session.get(Estudiante, estudiante_id)
    if not estudiante:
        raise HTTPException(status_code=404, detail="Estudiante no encontrado")
    return templates.TemplateResponse("estudiante/editar.html", {"request": request, "estudiante": estudiante})

# Ruta para procesar actualización de estudiante
@router.post("/editar/{estudiante_id}")
def actualizar_estudiante(
    request: Request,
    estudiante_id: int,
    nombre: str = Form(...),
    apellido: str = Form(...),
    edad: int = Form(...),
    correo: str = Form(...),
    genero: str = Form(...),
    codigo_estudiante: str = Form(...),
    session: Session = Depends(get_session)
):
    estudiante = session.get(Estudiante, estudiante_id)
    if not estudiante:
        raise HTTPException(status_code=404, detail="Estudiante no encontrado")

    # Actualizar datos del estudiante
    estudiante.nombre = nombre
    estudiante.apellido = apellido
    estudiante.edad = edad
    estudiante.correo = correo
    estudiante.genero = genero
    estudiante.codigo_estudiante = codigo_estudiante

    session.add(estudiante)
    session.commit()
    session.refresh(estudiante)

    return templates.TemplateResponse("estudiante/editar.html", {"request": request, "estudiante": estudiante, "mensaje": "Estudiante actualizado exitosamente"})

# Ruta para mostrar confirmación de eliminación
@router.get("/eliminar/{estudiante_id}")
def mostrar_confirmacion_eliminar(request: Request, estudiante_id: int, session: Session = Depends(get_session)):
    estudiante = session.get(Estudiante, estudiante_id)
    if not estudiante:
        raise HTTPException(status_code=404, detail="Estudiante no encontrado")
    return templates.TemplateResponse("estudiante/eliminar.html", {"request": request, "estudiante": estudiante})

# Ruta para eliminar estudiante
@router.post("/eliminar/{estudiante_id}")
def eliminar_estudiante(estudiante_id: int, session: Session = Depends(get_session)):
    estudiante = session.get(Estudiante, estudiante_id)
    if not estudiante:
        raise HTTPException(status_code=404, detail="Estudiante no encontrado")

    session.delete(estudiante)
    session.commit()
    return templates.TemplateResponse("estudiante/listar.html", {"request": {}, "mensaje": "Estudiante eliminado exitosamente"})
