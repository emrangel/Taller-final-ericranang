# from animal_exotico import Animal_Exotico
from models import animal_exotico, animal
# from animal import Animal

class Guarderia(animal.Animal):

    def __init__(self, list_hurones:list = [], list_boas:list = []) -> None:
        self.list_hurones = list_hurones
        self.list_boas = list_boas
    
    def alimentar_boas(self):
        for boas in self.list_boas:
            boas.comer_ratón()
        return "La boa está llena"
