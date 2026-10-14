with open("partida.txt", "w") as archivo:
    archivo.write("Nombre: TuNombre\n")
    archivo.write("XP: 350\n")
    archivo.write("Rango: Programador Junior\n")

with open("partida.txt", "r") as archivo:
    print(archivo.read())