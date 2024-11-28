from flask import jsonify, Blueprint
from models.huron import Huron
from models.perro import Perro
from models.gato import Gato
from models.boa_constructor import Boa_Constructor

# Blueprint de Flask
animales_blueprint = Blueprint('animales_bp', __name__, url_prefix="/animales")

# Mapeo de tipos de animales con sus respectivas clases
ANIMALES_MAP = {
    "huron": lambda: Huron("Pepe", 5, 5.2, "Zambia", 210.0),
    "boa": lambda: Boa_Constructor("Margarita", 8, 4.2, "Brasil", 2500.0),
    "gato": lambda: Gato("Felix", 3, 2.2),
    "perro": lambda: Perro("Lazzie", 8, 14.5)
}

def obtener_instancia_animal(tipo):
    """
    Devuelve una instancia del animal correspondiente al tipo.
    """
    constructor = ANIMALES_MAP.get(tipo)
    if not constructor:
        return None
    return constructor()

@animales_blueprint.route('/<tipo>', methods=["GET"])
def obtener_animal(tipo):
    """
    Devuelve los datos serializados del animal correspondiente al tipo.
    """
    animal = obtener_instancia_animal(tipo)
    if not animal:
        return "Tipo incorrecto", 400

    # data = {
    #     "data": animal.serializar()
    # }

    data = {
        "nombre": animal.nombre,
        "edad": animal.edad,
        "peso": animal.peso
    }
    return jsonify(data)

@animales_blueprint.route('/<tipo>/sonido', methods=["GET"])
def obtener_sonido_animal(tipo):
    """
    Devuelve el sonido que hace el animal correspondiente al tipo.
    """
    animal = obtener_instancia_animal(tipo)
    if not animal:
        return "Tipo incorrecto", 400

    # sonido = animal.hacer_sonido()
    # return jsonify({"data": sonido})

    data = {
        "data": animal.hacer_sonido()
    }
    return jsonify(data)
