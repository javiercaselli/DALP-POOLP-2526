# Expocoches

class zona():
    def __init__(self):
        self.libres = 0


    def comprobar(self):
        print (f"El número de entradas en esta zona es de {self.libres}")

    def vender(self, numero):
        if self.libres >= numero:
            self.libres -= numero
            print ("Aquí tiene sus entradas, gracias")
        else:
            print (f"Sólo me quedan {self.libres} entradas en esta zona")


class principal(zona):
    def __init__(self):
        super().__init__()
        self.libres = 1000

class compraventa(zona):
    def __init__(self):
        super().__init__()
        self.libres = 200

class vip(zona):
    def __init__(self):
        super().__init__()
        self.libres = 50


# Main
if __name__ == "__main__":
    principal = principal()
    compraventa = compraventa()
    vip = vip()

    opcion = 0
    while opcion != "3":
        print("EXPOCOCHES MÁLAGA")
        print()
        print("1. Mostrar número de entradas libres")
        print("2. Vender Entradas")
        print("3. Salir")

        opcion = input("Elige una opción: ")

        if opcion == "1":
            principal.comprobar()
            compraventa.comprobar()
            vip.comprobar()
        elif opcion == "2":
            ...
        else:
            print("Otra opción")