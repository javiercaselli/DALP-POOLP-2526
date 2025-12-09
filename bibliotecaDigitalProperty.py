from abc import ABC, abstractmethod
#---------------------------------
# Clase padre: RecursoDigital
#---------------------------------

class RecursoDigital(ABC):
    _contador_id = 1    # Variable de clase 

    def __init__(self, titulo, autor, anio):
        self.__id = RecursoDigital._contador_id
        RecursoDigital._contador_id += 1
        self.__titulo = None
        self.__autor = None
        self.__anio = None

        # Usaremos property para validación y encapsulamiento
        self.titulo = titulo
        self.autor = autor
        self.anio = anio

    # ----- id (read only) ----
    @property
    def id(self):
        return self.__id
    
    # ----- título -----
    @property
    def titulo(self):
        return self.__titulo

    @titulo.setter
    def titulo(self, nuevo_titulo):
        if not nuevo_titulo or not isinstance(nuevo_titulo, str):
            raise ValueError("El título debe ser un texto no vacío")
        self.__titulo = nuevo_titulo

    # ---- autor ----
    @property
    def autor(self):
        return self.__autor

    @autor.setter
    def autor(self, nuevo_autor):
        if not nuevo_autor or not isinstance(nuevo_autor, str):
            raise ValueError("El autor debe ser un texto no vacío")
        self.__autor = nuevo_autor

    @property
    def anio(self):
        return self.__anio

    @anio.setter
    def anio(self, nuevo_anio):
        if not isinstance(nuevo_anio, int) or not nuevo_anio > 0:
            raise ValueError("El anio debe ser un entero positivo")
        self.__anio = nuevo_anio

    # Método común
    def descripcion_basica(self):
        return f"Titulo: {self.titulo}, autor: {self.autor}, año: {self.anio}"

    # Metodo abrir (abstracto)
    @abstractmethod
    def abrir(self):
        pass

    # Método tipo (abstracto)
    @abstractmethod
    def tipo(self):
        pass

    # Método __str__
    def __str__(self):
        return f"[{self.id}] ({self.tipo()}) {self.descripcion_basica()}"


#---------------------------------
# Subclase: LibroDigital
#---------------------------------

class LibroDigital(RecursoDigital):
    def __init__(self, titulo, autor, anio, num_paginas, formato):
        super().__init__(titulo, autor, anio)
        self.__num_paginas = None
        self.__formato = None

        self.num_paginas = num_paginas
        self.formato = formato

    @property
    def num_paginas(self):
        return self.__num_paginas
    
    @num_paginas.setter
    def num_paginas(self, num_paginas):
        if not isinstance(num_paginas, int) or num_paginas < 0:
            raise ValueError("El número de páginas debe ser un entero positivo")
        self.__num_paginas = num_paginas

    @property
    def formato(self):
        return self.__formato
    
    @formato.setter
    def formato(self, formato):
        if not formato or not isinstance(formato, str):
            raise ValueError("El formato debe ser un texto no vacío")
        self.__formato = formato

    def abrir(self):
        return f"Abriendo libro '{self.titulo}' en formato {self.formato}..."
    
    def tipo(self):
        return "Libro"
    
    def __str__(self):
        return super().__str__() + f" - Nº Pags.: {self.num_paginas} - formato: {self.formato}"
    
#---------------------------------
# Subclase: Videocurso
#---------------------------------

class VideoCurso(RecursoDigital):
    def __init__(self, titulo, autor, anio, duracion, nivel):
        super().__init__(titulo, autor, anio)
        self.__duracion = None
        self.__nivel = None

        self.duracion = duracion
        self.nivel = nivel

    @property
    def duracion(self):
        return self.__duracion
    
    @duracion.setter
    def duracion(self, duracion):
        if not isinstance(duracion, int) or duracion < 0:
            raise ValueError("La duración debe ser un entero positivo")
        self.__duracion = duracion

    @property
    def nivel(self):
        return self.__nivel
    
    @nivel.setter
    def nivel(self, nivel):
        if not nivel or not isinstance(nivel, str):
            raise ValueError("El nivel debe ser un texto no vacío")
        self.__nivel = nivel

    def abrir(self):
        return f"Reproduciendo videoclase '{self.titulo}' nivel {self.nivel}, duración {self.duracion} min..."
    
    def tipo(self):
        return "Vídeo"
    
    def __str__(self):
        return super().__str__() + f" - duración: {self.duracion} minutos - nivel: {self.nivel}"
    
#---------------------------------
# Subclase: Podcast
#---------------------------------

class Podcast(RecursoDigital):
    def __init__(self, titulo, autor, anio, num_episodios, tema):
        super().__init__(titulo, autor, anio)
        self.__num_episodios = None
        self.__tema = None;
    
        self.num_episodios = num_episodios
        self.tema = tema

    @property
    def num_episodios(self):
        return self.__num_episodios
    
    @num_episodios.setter
    def num_episodios(self, num_episodios):
        if not isinstance(num_episodios, int) or num_episodios < 0:
            raise ValueError("El número de episodios debe ser un entero positivo")
        self.__num_episodios = num_episodios

    @property
    def tema(self):
        return self.__tema
    
    @tema.setter
    def tema(self, tema):
        if not tema or not isinstance(tema, str):
            raise ValueError("El tema debe ser un texto no vacío")
        self.__tema = tema

    def abrir(self):
        return f"Reproduciendo podcast '{self.titulo}' sobre {self.tema}, episodios {self.num_episodios}..."
    
    def tipo(self):
        return "Podcast"
    
    def __str__(self):
        return super().__str__() + f" - Nº episodios: {self.num_episodios} - tema: {self.tema}"
    

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
        for recurso in self.__recursos:
            print (recurso)
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
    libro1.anio = 2024
    print("Cambiando el nivel del vídeo...")
    video1.nivel = "Avanzado"
    print()
    biblio.listar_recursos()

