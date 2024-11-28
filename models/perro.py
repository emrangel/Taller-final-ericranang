from abc import ABC
from models.animal import Animal
# from models import animal_exotico

# Clase que representa un perro
class Perro(Animal):
    #Constructor
    def __init__(self, nombre: str, edad: int, peso: float) -> None:
        super().__init__(nombre, edad, peso)

    #Métodos
    def hacer_sonido(self):
        return "¡Guau guau!"