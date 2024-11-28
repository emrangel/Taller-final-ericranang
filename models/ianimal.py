from abc import ABC, abstractmethod

class IAnimal(ABC):
    
    @abstractmethod
    def hacer_sonido(self):
        pass
