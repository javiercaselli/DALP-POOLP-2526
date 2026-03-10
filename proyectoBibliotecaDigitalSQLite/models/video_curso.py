from .recurso_digital import RecursoDigital
from typing import Dict, Any

#---------------------------------
# Subclase: Videocurso
#---------------------------------

class VideoCurso(RecursoDigital):
    def __init__(self, id, titulo, autor, anio, duracion, nivel):
        super().__init__(id, titulo, autor, anio)
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
        return "VideoCurso"
    
    def __str__(self):
        return super().__str__() + f" - duración: {self.duracion} minutos - nivel: {self.nivel}"
    
        # -------- JSON ---------
    #Convierte la instancia de esta clase en una estructura Dict.
    def to_dict(self) -> Dict[str, Any]:
        d = super().to_dict()
        d.update({
            "duracion": self.duracion,
            "nivel": self.nivel
        })

        return d
    
    #Convierte una estructura Dict en una instancia de la presente clase
    @staticmethod
    def from_dict(data: Dict[str, Any]) -> "RecursoDigital":
        return VideoCurso(
            id = int(data["id"]),
            titulo=str(data["titulo"]),
            autor=str(data["autor"]),
            anio=int(data["anio"]),
            duracion=int(data["duracion"]),
            nivel=str(data["nivel"])
        )

    
