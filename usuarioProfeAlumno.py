from abc import ABC, abstractmethod

# Clase base ------------------------------------------------------

class Usuario(ABC):
    def __init__(self, nombre, email):
        # Encapsulación: atributos privados
        self.__nombre = nombre
        self.__email = email

    # Getters y setters (encapsulación)
    def get_nombre(self):
        return self.__nombre

    def set_nombre(self, nuevo_nombre):
        self.__nombre = nuevo_nombre

    def get_email(self):
        return self.__email

    def set_email(self, nuevo_email):
        self.__email = nuevo_email

    # Método común
    @abstractmethod
    def presentacion(self):
        pass


# Subclase Alumno -------------------------------------------------

class Alumno(Usuario):
    def __init__(self, nombre, email, curso, nota_media):
        # Llamamos al constructor de Usuario
        super().__init__(nombre, email)
        self.curso = curso
        self.nota_media = nota_media

    # Polimorfismo: sobrescribimos presentacion()
    def presentacion(self):
        return (f"Soy {self.get_nombre()}, estudiante de {self.curso}, "
                f"con una nota media de {self.nota_media}.")


# Subclase Profesor -----------------------------------------------

class Profesor(Usuario):
    def __init__(self, nombre, email, especialidad):
        super().__init__(nombre, email)
        self.especialidad = especialidad

    # Polimorfismo: sobrescribimos presentacion()
    def presentacion(self):
        return (f"Soy el profesor {self.get_nombre()}, "
                f"especialista en {self.especialidad}.")


# Uso del polimorfismo --------------------------------------------

usuarios = [
    Alumno("Lucía", "lucia@mail.com", "CE Python", 8.5),
    Alumno("Carlos", "carlos@mail.com", "1º DAW", 7.3),
    Profesor("Javier", "j.casas@example.com", "Programación"),
    Profesor("Ana", "ana@example.com", "Bases de Datos")
    #Usuario("Pepe", "si@claro.es")
]

for u in usuarios:
    print(u.presentacion())