class Perro:
    def __init__(self, nombre):
        self.nombre = nombre


class Mineral:
    def __init__(self, nombre):
        self.nombre = nombre

class Caballo:
    def __init__(self, nombre, edad):
        self.nombre = nombre
        self.edad = edad

    def decirNombre(self):
        print(f"Hola, me llamo {self.nombre}")

    def cabalgar(self):
        print(f"Tocotoc, tocotoc, tocotoc")

    def relinchar(self):
        print(f"Hiiiiiieeeeeee!!")


class Gato:
    def __init__(self, nombre):
        self.nombre = nombre


class Animal:
    def __init__(self, nombre):
        self.nombre = nombre

class Persona:
    def __init__(self, nombre):
        self.nombre = nombre

class Vehiculo:
    vehiculosCreados = 0
    kilometrosTotales = 0

    def __init__(self, kilometrosRecorridos):
        self.kilometrosRecorridos = kilometrosRecorridos

    def andar(self, kilometros):
        self.kilometrosTotales += kilometros
        

class Bicicleta(Vehiculo):
    def __init__(self):
        super().__init__()

    def caballito(self):
        print(f"Yuhuuu!")

class Coche(Vehiculo):
    def __init__(self):
        super().__init__()

    def quemarRueda(self):
        print(f"Vrum!")



if __name__ == "__main__":
    personas = Persona("Paula")
    perros = Perro("Goofy")

    caballo1 = Caballo("Babieca", 5)
    caballo2 = Caballo("Bucéfalo", 7)

    caballo1.decirNombre()
    caballo2.decirNombre()
    caballo2.cabalgar()
    caballo1.relinchar()