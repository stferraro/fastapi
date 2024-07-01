from math import sqrt
from fastapi import FastAPI
from pydantic import BaseModel

app = FastAPI()

class Rombo(BaseModel):
    diagMayor: float
    diagMenor: float

@app.post("/rombo")
def calcular_area_y_perimetro(rombo: Rombo):
    area = round((rombo.diagMayor * rombo.diagMenor) / 2,2)
    lado = round(sqrt((rombo.diagMenor**2 + rombo.diagMayor**2)/2),2) 
    perimetro = round(4 * (lado),2)

    return {
        "area": area,
        "perimetro": perimetro
    }