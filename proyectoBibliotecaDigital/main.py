from __future__ import annotations
from models import RecursoDigital, LibroDigital, VideoCurso, Podcast
from services import BibliotecaDigital
from persistence.json_manager import guardar_recursos, cargar_recursos

RUTA_JSON = "proyectoBibliotecaDigital/data/recursos.json"

# Muestra el menú por pantalla
def mostrar_menu() -> None:
    print("\n===Biblioteca de Recursos Digitales (Entrega 2 - JSON)===")
    print("1. Listar Recursos")
    print("2. Añadir recursos (demo)")
    print("3. Guardar en JSON")
    print("4. Cargar desde JSON (reemplaza la lista actual)")
    print("5. Salir")

#Prueba de creación de recurso
def alta_demo(bilio:BibliotecaDigital) -> None:
    nuevo = Podcast(
        titulo="Python en producción",
        autor="CE DALP",
        anio=2026,
        num_episodios=1,
        tema="Programación"
    )
    biblio.agregar_recurso(nuevo)
    print("Recurso añadido: ", nuevo)

#---------------------------------
# Programa principal (main)
#---------------------------------
if __name__ == "__main__":
    biblio = BibliotecaDigital("Mi Biblio")

    #Carga automática al iniciar la aplicación
    recursos = cargar_recursos(RUTA_JSON)
    biblio.reemplazar_todos(recursos)
    print (f"Cargados {len(recursos)} recursos desde {RUTA_JSON}")









   