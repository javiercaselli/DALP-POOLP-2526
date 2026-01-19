from __future__ import annotations
from models import RecursoDigital, LibroDigital, VideoCurso, Podcast
from services import BibliotecaDigital

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

