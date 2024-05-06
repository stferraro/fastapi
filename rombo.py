from math import sqrt
from fastapi import FastAPI
from pydantic import BaseModel

app = FastAPI()

class Rombo(BaseModel):
    diagMayor: float
    diagMenor: float

@app.post("/rombo")
def calcular_area_y_perimetro(rombo: Rombo):
    area = (rombo.diagMayor * rombo.diagMenor) / 2
    lado = sqrt((rombo.diagMenor**2 + rombo.diagMayor**2)/2) 
    perimetro = 4 * (lado)

    return {
        "area": area,
        "perimetro": perimetro
    }