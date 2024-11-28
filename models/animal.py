from abc import abstractmethod
# from ianimal import IAnimal
from models import ianimal

class Animal(ianimal.IAnimal):
    def __init__(self, nombre: str, peso: float, edad: int) -> None:
        self._nombre = nombre
        self._peso = peso
        self._edad = edad

    # Getters y setters para nombre
    @property
    def nombre(self) -> str:
        return self._nombre

    @nombre.setter
    def nombre(self, value: str) -> None:
        if isinstance(value, str):
            self._nombre = value
        else:
            raise ValueError('Expected str')

    # Getters y setters para peso
    @property
    def peso(self) -> float:
        return self._peso

    @peso.setter
    def peso(self, value: float) -> None:
        if isinstance(value, float):
            self._peso = value
        else:
            raise ValueError('Expected float')

    # Getters y setters para edad
    @property
    def edad(self) -> int:
        return self._edad

    @edad.setter
    def edad(self, value: int) -> None:
        if isinstance(value, int):
            self._edad = value
        else:
            raise ValueError('Expected int')

    # Método abstracto
    def hacer_sonido(self):
        pass
