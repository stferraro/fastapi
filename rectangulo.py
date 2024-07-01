from fastapi import FastAPI
from pydantic import BaseModel

app = FastAPI()

class Rectangulo(BaseModel):
    base: float
    altura: float

@app.post("/rectangulo")
def calcular_area_y_perimetro(rectangulo: Rectangulo):
    area = rectangulo.base * rectangulo.altura
    perimetro = 2 * (rectangulo.base + rectangulo.altura)

    return {
        "area": area,
        "perimetro": perimetro
    }