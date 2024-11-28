from boa_constructor import Boa_Constructor
from huron import Huron

# Pruebas para la boa
boa = Boa_Constructor("Boa Constructor", 12.5, 5, "Brasil", 10.0)
print(boa.hacer_sonido())  # ¡Tsss!
boa.comer_ratón()
print(f"Ratones comidos: {boa.ratones_comidos}")  # Ratones comidos: 1
print(f"Costo de flete: {boa.calcular_flete()}")  # Costo de flete: 125.0

# Pruebas para el hurón
huron = Huron("Hurón", 1.5, 2, "Canadá", 5.0)
print(huron.hacer_sonido())  # ¡Eek Eek!
print(f"Costo de flete: {huron.calcular_flete()}")  # Costo de flete: 7.5
