# from animal_exotico import Animal_Exotico
from models import animal_exotico

class Huron(animal_exotico.Animal_Exotico):
    def hacer_sonido(self):
        return "¡Eek Eek!"
