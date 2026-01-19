from .recurso_digital import RecursoDigital

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
    
