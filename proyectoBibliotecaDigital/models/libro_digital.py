from .recurso_digital import RecursoDigital

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
