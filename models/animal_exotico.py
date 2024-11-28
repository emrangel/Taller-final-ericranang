# from animal import Animal
from models import animal
from abc import abstractmethod

class Animal_Exotico(animal.Animal):
    def __init__(self, nombre: str, peso: float, edad: int, pais_origen: str, impuestos: float) -> None:
        super().__init__(nombre, peso, edad)
        self._pais_origen = pais_origen
        self._impuestos = impuestos

    # Getters y setters para pais_origen
    @property
    def pais_origen(self) -> str:
        return self._pais_origen

    @pais_origen.setter
    def pais_origen(self, value: str) -> None:
        if isinstance(value, str):
            self._pais_origen = value
        else:
            raise ValueError('Expected str')

    # Getters y setters para impuestos
    @property
    def impuestos(self) -> float:
        return self._impuestos

    @impuestos.setter
    def impuestos(self, value: float) -> None:
        if isinstance(value, float):
            self._impuestos = value
        else:
            raise ValueError('Expected float')

    # Método para calcular flete
    def calcular_flete(self) -> float:
        return self._impuestos * self.peso

