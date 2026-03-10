from __future__ import annotations

from typing import List, Optional
from models import RecursoDigital

class BibliotecaDigital:
    def __init__(self, nombre) -> None:
        self.__nombre = nombre
        self.__recursos = []

    def agregar_recurso(self, recurso) -> None:
        self.__recursos.append(recurso)

    def listar_recursos(self) -> List[RecursoDigital]:
        return self.__recursos

    def abrir_todos(self) -> None:
        print("=== Abriendo todos los recursos ===")
        for recurso in self.__recursos:
            print(recurso.abrir())

    def reemplazar_todos(self, recursos: List[RecursoDigital]) -> None:
        self.__recursos = list(recursos)


    def buscar_por_id(self, id: int) -> Optional[RecursoDigital]:
        for r in self.__recursos:
            if r.id == id:
                return r
        return None
    
    def borrar_recurso(self, id: int) -> bool:
        recurso = self.buscar_por_id(id)

        if not recurso:
            return False
        else:
            self.__recursos.remove(recurso)
            return True