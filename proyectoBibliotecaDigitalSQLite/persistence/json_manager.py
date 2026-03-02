from __future__ import annotations

import json
import os
from typing import List

from models import RecursoDigital

# Volcado a fichero JSON de las Biblioteca Digital
def guardar_recursos(ruta_fichero: str, recursos: List[RecursoDigital]) -> None:
    data = [r.todict() for r in recursos]
    os.makedirs(os.path.dirname(ruta_fichero), exist_ok=True)

    with open(ruta_fichero, "w", encoding="utf-8") as f:
        json.dump(data, f, ensure_ascii=False, indent=2)


# Recuperación de la Biblioteca Digital desde un fichero JSON
def cargar_recursos(ruta_fichero: str) -> List[RecursoDigital]:
    print("CWD: ", os.getcwd())
    print("Buscando:", os.path.abspath(ruta_fichero))
    if not os.path.exists(ruta_fichero):
        return []

    with open(ruta_fichero, "r", encoding="utf-8") as f:
        contenido = json.load(f)

    if not isinstance(contenido, list):
        raise ValueError("El JSON debe contener una lista de recursos.")
    
    recursos : List[RecursoDigital] = []

    for item in contenido:
        if not isinstance(item, dict):
            raise ValueError("Cada recurso del JSON debe ser un objeto diccionario (dict)")
        
        recursos.append(RecursoDigital.from_dict(item))

    return recursos
