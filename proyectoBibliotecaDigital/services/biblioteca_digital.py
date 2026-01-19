class BibliotecaDigital:
    def __init__(self, nombre):
        self.__nombre = nombre
        self.__recursos = []

    def agregar_recurso(self, recurso):
        self.__recursos.append(recurso)

    def listar_recursos(self):
        for recurso in self.__recursos:
            print (recurso)
    def abrir_todos(self):
        print("=== Abriendo todos los recursos ===")
        for recurso in self.__recursos:
            print(recurso.abrir())
