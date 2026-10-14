class Jugador:
    def __init__(self, nombre, rango):
        self.nombre = nombre
        self.rango = rango

# Fuera de la clase creas el objeto e imprimes sus atributos
mi_jugador = Jugador("TuNombre", "Programador Junior")
print(mi_jugador.nombre)
print(mi_jugador.rango)