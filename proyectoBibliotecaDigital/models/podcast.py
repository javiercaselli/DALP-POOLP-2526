from .recurso_digital import RecursoDigital

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
