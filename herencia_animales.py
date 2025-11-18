# herencia_animales.py

# Clase Animal (padre)
from abc import ABC, abstractmethod


class Mamifero(ABC):
    def __init__(self, nombre):
        self.nombre = nombre;

    @abstractmethod
    def hablar(self):
        pass    # Obliga a la subclases (o clases hijas) a implementar este método
    
    def respirar(self):
        return "Fffffffff"
    
# Clases hijas
class Perro(Mamifero):
    def hablar(self):
        return "Guau!"
    
class Gato(Mamifero):
    def afilarUnias(self):
        return "Ras!!"
    
    def hablar(self):
        return "Miau!"
    
class Conejo(Mamifero):
    def hablar(self):
        return "Guuuu!"



# Programa principal
if __name__ == "__main__":
    animales = [Perro("Toby"), Gato("Misifú"), Conejo("Mango")]

    for a in animales:
        print(f"{a.nombre}: {a.hablar()}")

    for a in animales:
        print(f"{a.nombre}: {a.respirar()}")