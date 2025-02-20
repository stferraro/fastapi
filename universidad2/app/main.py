from fastapi import FastAPI
from fastapi.templating import Jinja2Templates
from starlette.requests import Request
from fastapi.staticfiles import StaticFiles
from app.routes import router  # Aquí importas el router que contiene tus rutas

# Crear la aplicación FastAPI
app = FastAPI()

# Configurar las plantillas (HTML) usando Jinja2
templates = Jinja2Templates(directory="app/templates")

# Incluir las rutas
app.include_router(router)  # Aquí incluyes las rutas


# Ruta para servir el archivo index.html
@app.get("/")
async def read_index(request: Request):
    return templates.TemplateResponse("index.html", {"request": request})
