# coding: utf-8

from fastapi import APIRouter
from .estudiantes_routes import router as estudiante_router

router = APIRouter()

# Incluir las rutas de estudiantes
router.include_router(estudiante_router)
