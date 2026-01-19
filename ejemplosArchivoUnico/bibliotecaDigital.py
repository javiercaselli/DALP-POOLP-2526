from abc import ABC, abstractmethod
#---------------------------------
# Clase padre: RecursoDigital
#---------------------------------

class RecursoDigital(ABC):
    def __init__(self, titulo, autor, anio):
        self.__titulo = titulo
        self.__autor = autor
        self.__anio = anio

    # Getters y setters
    def get_titulo(self):
        return self.__titulo

    def set_titulo(self, nuevo_titulo):
        self.__titulo = nuevo_titulo

    def get_autor(self):
        return self.__autor

    def set_autor(self, nuevo_autor):
        self.__autor = nuevo_autor

    def get_anio(self):
        return self.__anio

    def set_anio(self, nuevo_anio):
        self.__anio = nuevo_anio

    # Método común
    def descripcion_basica(self):
        return f"Titulo: {self.__titulo}, autor: {self.__autor}, año: {self.__anio}"

    # Metodo abrir (abstracto)
    @abstractmethod
    def abrir(self):
        pass

    # Método tipo (abstracto)
    @abstractmethod
    def tipo(self):
        pass


#---------------------------------
# Subclase: LibroDigital
#---------------------------------

class LibroDigital(RecursoDigital):
    def __init__(self, titulo, autor, anio, num_paginas, formato):
        super().__init__(titulo, autor, anio)
        self.__num_paginas = num_paginas
        self.__formato = formato;

    def abrir(self):
        return f"Abriendo libro '{self.get_titulo()}' en formato {self.__formato}..."
    
    def tipo(self):
        return "Libro"
    
#---------------------------------
# Subclase: Videocurso
#---------------------------------

class VideoCurso(RecursoDigital):
    def __init__(self, titulo, autor, anio, duracion, nivel):
        super().__init__(titulo, autor, anio)
        self.__duracion = duracion
        self.__nivel = nivel;

    def abrir(self):
        return f"Reproduciendo videoclase '{self.get_titulo()}' nivel {self.__nivel}, duración {self.__duracion} min..."
    
    def tipo(self):
        return "Vídeo"
    
#---------------------------------
# Subclase: Podcast
#---------------------------------

class Podcast(RecursoDigital):
    def __init__(self, titulo, autor, anio, num_episodios, tema):
        super().__init__(titulo, autor, anio)
        self.__num_episodios = num_episodios
        self.__tema = tema;

    def abrir(self):
        return f"Reproduciendo podcase '{self.get_titulo()}' sobre {self.__tema}, episodios {self.__num_episodios}..."
    
    def tipo(self):
        return "Podcast"
    

#---------------------------------
# Clase BibliotecaDigital
#---------------------------------

class BibliotecaDigital:
    def __init__(self, nombre):
        self.__nombre = nombre
        self.__recursos = []

    def agregar_recurso(self, recurso):
        self.__recursos.append(recurso)

    def listar_recursos(self):
        for i, recurso in enumerate(self.__recursos, start=1):
            print (f"{i}. ({recurso.tipo()}) - {recurso.descripcion_basica()}")
    def abrir_todos(self):
        print("=== Abriendo todos los recursos ===")
        for recurso in self.__recursos:
            print(recurso.abrir())


#---------------------------------
# Programa principal (main)
#---------------------------------
if __name__ == "__main__":
    # Crear algunos recursos
    libro1 = LibroDigital("Python desde cero", "Ana López", 2022, 350, "PDF")
    video1 = VideoCurso("POO en Python", "Javier Caselli", 2023, 90, "Intermedio")
    podcast1 = Podcast("Tecnología hoy", "Laura Gómez", 2021, 24, "Innovación")

    # Crear la biblioteca y añadir recursos
    biblio = BibliotecaDigital("Biblioteca FP Informática")
    biblio.agregar_recurso(libro1)
    biblio.agregar_recurso(video1)
    biblio.agregar_recurso(podcast1)

    # Listar recursos
    biblio.listar_recursos()
    print()

    # Abrir todos los recursos
    biblio.abrir_todos()
    print()

    # Probar la encapsulación: cambiar el año de un recurso
    print("Cambiando el año del libro...")
    libro1.set_anio(2024)
    biblio.listar_recursos()