from .recurso_digital import RecursoDigital
from typing import Dict, Any

#---------------------------------
# Subclase: LibroDigital
#---------------------------------

class LibroDigital(RecursoDigital):
    def __init__(self, titulo, autor, anio, num_paginas, formato, isbn):
        super().__init__(titulo, autor, anio)
        self.__num_paginas = None
        self.__formato = None
        self.__isbn = None

        self.num_paginas = num_paginas
        self.formato = formato
        self.isbn = isbn

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

    @property
    def isbn(self):
        return self.__isbn
    
    @isbn.setter
    def isbn(self, isbn):
        if not isbn or not isinstance(isbn, int):
            raise ValueError("El ISBN debe ser un número entero")

    def abrir(self):
        return f"Abriendo libro '{self.titulo}' en formato {self.formato}..."
    
    def tipo(self):
        return "Libro"
    
    def __str__(self):
        return super().__str__() + f" - Nº Pags.: {self.num_paginas} - formato: {self.formato}"
    
    # -------- JSON ---------
    #Convierte la instancia de esta clase en una estructura Dict.
    def to_dict(self) -> Dict[str, Any]:
        d = super().to_dict()
        d.update({
            "num_paginas": self.num_paginas,
            "formato": self.formato,
            "isbn": self.isbn
        })

        return d
    
    #Convierte una estructura Dict en una instancia de la presente clase
    @staticmethod
    def from_dict(data: Dict[str, Any]) -> "RecursoDigital":
        return LibroDigital(
            recurso_id = int(data["recurso_id"]),
            titulo=str(data["titulo"]),
            autor=str(data["autor"]),
            anio=int(data["anio"]),
            num_paginas=int(data["num_paginas"]),
            formato=str(data["formato"]),
            isbn=str(data["isbn"])
        )

