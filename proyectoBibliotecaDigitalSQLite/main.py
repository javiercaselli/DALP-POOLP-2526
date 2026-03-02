from __future__ import annotations
from models import RecursoDigital, LibroDigital, VideoCurso, Podcast
from services import BibliotecaDigital
from persistence.json_manager import guardar_recursos, cargar_recursos
from persistence.sqlite_manager import init_db

RUTA_JSON = "proyectoBibliotecaDigitalSQLite/data/recursos.json"
RUTA_DB = "proyectoBibliotecaDigitalSQLite/data/recursos.db"

#1 Muestra el menú por pantalla
def mostrar_menu() -> None:
    print("\n===Biblioteca de Recursos Digitales (Entrega 3 - SQLite)===")
    print("1. Listar Recursos")
    print("2. Añadir recursos (demo)")
    print("3. Guardar en JSON")
    print("4. Cargar desde JSON (reemplaza la lista actual)")
    print("5. Salir")

#2 Crear esquema si no existe
init_db(RUTA_DB)

#3 Imprime el menú
mostrar_menu()








   