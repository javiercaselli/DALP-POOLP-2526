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

