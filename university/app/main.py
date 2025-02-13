from fastapi import FastAPI
from fastapi.staticfiles import StaticFiles
from app.routes.estudiantes import router as estudiantes_router

app = FastAPI()

app.mount("/static", StaticFiles(directory="app/static"), name="static")

app.include_router(estudiantes_router)

@app.get("/")
async def read_root():
    return {"message": "Bienvenido a la API de la Universidad"}