import random

class Jugador:
    def __init__(self, nombre, vida=100, oro=50):
        self.nombre = nombre
        self.vida = vida
        self.oro = oro

    def atacar(self, enemigo):
        dano = random.randint(10, 20)
        enemigo.vida -= dano
        print(f"⚔️ {self.nombre} atacó a {enemigo.nombre} y le causó {dano} de daño!")
        return dano

    def mostrar_stats(self):
        print(f"🛡️ Héroe: {self.nombre} | HP: {self.vida} | Oro: {self.oro} 🪙")

# Creación de la instancia y prueba
mi_jugador = Jugador("Alex")
mi_jugador.mostrar_stats()