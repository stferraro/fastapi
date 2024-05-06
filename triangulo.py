from fastapi import FastAPI
from math import sqrt

app = FastAPI()

@app.get("/area_triangulo/{lado1}/{lado2}/{lado3}")
def area_triangulo(lado1: float, lado2: float, lado3: float):
    """
    Esta función calcula el área de un triángulo dados los lados.
    """
    s = (lado1 + lado2 + lado3) / 2
    area = sqrt(s * (s - lado1) * (s - lado2) * (s - lado3))
    return {"area": area}