from abc import ABC
from models.animal import Animal

# Clase que representa un gato
class Gato(Animal):
    #Constructor
    def __init__(self, nombre: str, edad: int, peso: float) -> None:
        super().__init__(nombre, edad, peso)

    #Métodos
    def hacer_sonido(self):
        return "¡Miau Miau!"