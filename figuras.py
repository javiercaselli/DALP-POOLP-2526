from abc import ABC, abstractmethod

class Figura(ABC):

    @abstractmethod
    def area(self):
        pass


class cuadrado(Figura):
    def __init__(self, lado):
        self.lado = lado

    def area(self):
        return (self.lado*self.lado)
    

class circulo(Figura):
    def __init__(self, radio):
        self.radio = radio

    def area(self):
        return 3.1516 * self.radio ** 2
    


# Programa principal 
if __name__ == "__main__":
    figuras = [cuadrado(3), circulo(3)]
    
    for f in figuras:
        print(f"{f.area()}")
