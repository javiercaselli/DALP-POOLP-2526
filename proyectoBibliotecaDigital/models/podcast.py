from .recurso_digital import RecursoDigital
from typing import Dict, Any


#---------------------------------
# Subclase: Podcast
#---------------------------------

class Podcast(RecursoDigital):
    def __init__(self, id, titulo, autor, anio, episodio, url):
        super().__init__(id, titulo, autor, anio)
        self.__episodio = None
        self.__url = None;
    
        self.episodio = episodio
        self.url = url

    @property
    def episodio(self):
        return self.__episodio
    
    @episodio.setter
    def episodio(self, episodio):
        if not isinstance(episodio, int) or episodio < 0:
            raise ValueError("El número de episodio debe ser un entero positivo")
        self.__episodio = episodio

    @property
    def url(self):
        return self.__url
    
    @url.setter
    def url(self, url):
        if not url or not isinstance(url, str):
            raise ValueError("El url debe ser un texto no vacío")
        self.__url = url

    def abrir(self):
        return f"Reproduciendo podcast '{self.titulo}' sobre {self.url}, episodio {self.episodio}..."
    
    def tipo(self):
        return "Podcast"
    
    def __str__(self):
        return super().__str__() + f" - Nº episodio: {self.episodio} - url: {self.url}"

    # -------- JSON ---------
    #Convierte la instancia de esta clase en una estructura Dict.
    def to_dict(self) -> Dict[str, Any]:
        d = super().to_dict()
        d.update({
            "episodio": self.episodio,
            "url": self.url
        })

        return d
    
    #Convierte una estructura Dict en una instancia de la presente clase
    @staticmethod
    def from_dict(data: Dict[str, Any]) -> "RecursoDigital":
        return Podcast(
            id = int(data["id"]),
            titulo=str(data["titulo"]),
            autor=str(data["autor"]),
            anio=int(data["anio"]),
            episodio=int(data["episodio"]),
            url=str(data["url"])
        )
