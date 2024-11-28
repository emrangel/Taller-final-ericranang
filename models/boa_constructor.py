# from animal_exotico import Animal_Exotico
from models import animal_exotico

class Boa_Constructor(animal_exotico.Animal_Exotico):
    def __init__(self, nombre: str, peso: float, edad: int, pais_origen: str, impuestos: float) -> None:
        super().__init__(nombre, peso, edad, pais_origen, impuestos)
        self.ratones_comidos = 0  # Inicializamos a 0
    
    @property
    def ratones_comidos(self) -> int:
        """ Devuelve el valor del atributo privado 'ratones_comidos' """
        return self._ratones_comidos
    
    @ratones_comidos.setter
    def ratones_comidos(self, value:int) -> None:
        """ 
        Establece un nuevo valor para el atributo privado 'ratones_comidos'
    
        Valida que el valor enviado corresponda al tipo de dato del atributo
        """ 
        if isinstance(value, int):
            self._ratones_comidos = value
        else:
            raise ValueError('Expected int')
    
    def dar_ratones_comidos(self) -> int:
        return self.ratones_comidos()

    # Método para incrementar la cuenta de ratones
    def comer_raton(self) -> None:
        if self._ratones_comidos == 10:
            raise ValueError("Demasiados Ratones!")
        else:
            self._ratones_comidos += 1

    # Redefinir el método hacer_sonido
    def hacer_sonido(self):
        return "¡Tsss!"
