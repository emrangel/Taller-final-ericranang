import unittest
from models import huron, boa_constructor, animal_exotico, guarderia

class TestUser(unittest.TestCase):

    def test_hacer_ruido_huron(self):
        hurons = huron.Huron("Hurón", 1.5, 2, "Canadá", 5.0)
        self.assertEqual(hurons.hacer_sonido(), "¡Eek Eek!")

    def test_hacer_ruido_boa(self):
        boas = boa_constructor.Boa_Constructor("Boa Constructor", 12.5, 5, "Brasil", 10.0)
        self.assertEqual(boas.hacer_sonido(), "¡Tsss!")

    def test_flete_huron(self):
        huron = huron.Huron("Hurón", 1.5, 2, "Canadá", 5.0)
        self.assertEqual(huron.calcular_flete(), 7.5)

    def test_flete_boa(self):
        boa = boa_constructor.Boa_Constructor("Boa Constructor", 12.5, 5, "Brasil", 10.0)
        self.assertEqual(boa.calcular_flete(), 125.0)

    def test_alimentar_boa(self):
        boa = boa_constructor.Boa_Constructor("Boa Constructor", 12.5, 5, "Brasil", 10.0)
        boa.comer_raton()
        self.assertEqual(boa.ratones_comidos, 1)

    def test_guarderia(self):

        guarderias = guarderia.Guarderia()
        huron1 = huron.Huron("Hurón1", 1.5, 2, "Canadá", 5.0)
        huron2 = huron.Huron("Hurón2", 1.5, 2, "Canadá", 5.0)

        boa1 = boa_constructor.Boa_Constructor("Boa Constructor1", 12.5, 5, "Brasil", 10.0)
        boa2 = boa_constructor.Boa_Constructor("Boa Constructor2", 12.5, 5, "Brasil", 10.0)

        guarderias.list_hurones.append(huron1)
        guarderias.list_hurones.append(huron2)
        guarderias.list_hurones.append(boa1)
        guarderias.list_hurones.append(boa2)

        try:
            guarderia_boas = guarderias.alimentar_boas()
            self.assertEqual(guarderia_boas, "La boa está llena")
        except ValueError as e:
            self.assertEqual(str(e), "Demasiados Ratones")

