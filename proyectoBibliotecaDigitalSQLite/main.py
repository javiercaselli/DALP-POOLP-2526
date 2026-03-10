from __future__ import annotations
from models import RecursoDigital, LibroDigital, VideoCurso, Podcast
from services import BibliotecaDigital
#from persistence.json_manager import guardar_recursos, cargar_recursos
from persistence.sqlite_manager import init_db, cargar_recursos, guardar_recursos

RUTA_JSON = "proyectoBibliotecaDigitalSQLite/data/recursos.json"
RUTA_DB = "proyectoBibliotecaDigitalSQLite/data/recursos.db"

#1 Muestra el menú por pantalla
def mostrar_menu() -> None:
    print("\n===Biblioteca de Recursos Digitales (Entrega 3 - SQLite)===")
    print("1. Listar Recursos")
    print("2. Añadir recursos")
    print("3. Borrar recurso")
    print("4. Guardar en Base de datos")
    print("5. Cargar desde Base de datos (reemplaza la lista actual)")
    print("6. Salir")

#2 Listar recursos
def listar_recursos(biblioteca: BibliotecaDigital) -> None:
    recursos = biblioteca.listar_recursos()

    if not recursos:
        print("No hay recursos en la biblioteca")
        return
    
    print("--- LISTADO DE RECURSOS ---")
    for recurso in recursos:
        print(recurso)

#3 Añadir recurso
def anadir_recurso(biblioteca: BibliotecaDigital) -> None:
    recurso = crear_recurso_desde_teclado()

    if recurso is None:
        return
    
    biblioteca.agregar_recurso(recurso)

    print("Recurso añadido correctamente")

#3.1 Obtiene información del usuario para crear un nuevo recurso
def crear_recurso_desde_teclado() -> RecursoDigital:
    print("\n¿Qué tipo de recurso desea añadir?")
    print("1. Libro digital")
    print("2. Vídeo curso")
    print("3. Podcast")

    opcion = input("Elige una opción: ").strip()

    titulo = input("Título: ").strip()
    autor = input("Autor: ").strip()
    anio = pedir_entero("Año: ")

    match opcion:
        case "1":
            isbn = input("ISBN: ").strip()
            num_paginas = pedir_entero("Número de páginas: ")
            formato = input("Formato: ").strip()

            return LibroDigital(
                None,
                titulo,
                autor,
                anio,
                num_paginas, 
                formato, 
                isbn
            )
        
        case "2":
            duracion = pedir_entero("Duración en minutos: ")
            nivel = input("Nivel (Básico, Intermedio, Avanzado): ").strip()

            return VideoCurso(
                None,
                titulo,
                autor,
                anio,
                duracion,
                nivel
            )

        case "3":
            episodio = pedir_entero("Número de episodio: ")
            url = input("URL: ").strip()

            return VideoCurso(
                None,
                titulo,
                autor,
                anio,
                episodio,
                url
            )
        
        case _:
            print("Opción no válida")
            return None

#3.2 Pedir un número entero desde teclado        
def pedir_entero(mensaje: str) -> int:
    while True:
        try:
            return int(input(mensaje))
        except ValueError:
            print("Error: debes introducir un número entero")

#4 Borrar un recurso
def borrar_recurso(biblioteca : BibliotecaDigital):
    id_recurso = pedir_entero("Introduce el ID del recurso a borrar: ")

    if not biblioteca.borrar_recurso(id_recurso):
        print("ERROR: No existe ningún recurso con ese ID")
    else:
        print("Recurso eliminado correctamente")

#5 Cuerpo del main
def main() -> None:
    #1 Crear esquema si no existe
    init_db(RUTA_DB)

    #2 Crear una biblioteca digital (almacenamiento en memoria)
    biblioteca = BibliotecaDigital("biblio dalp 2026")

    #3 Muestra menú
    while True:
        mostrar_menu()
        opcion = input("Selecciona una opción: ").strip()

        if opcion == "1":
            listar_recursos(biblioteca)
        elif opcion == "2":
            anadir_recurso(biblioteca)
        elif opcion == "3":
            borrar_recurso(biblioteca)
        elif opcion == "4":
            guardar_recursos(RUTA_DB, biblioteca.listar_recursos())
            print("Recursos guardados correctamente en la Base de Datos")
        elif opcion == "5":
            recursos = cargar_recursos(RUTA_DB)
            biblioteca.reemplazar_todos(recursos)
            print("Recursos cargos correctamente desde la base de datos")
        elif opcion == "6":
            print("Saliendo del programa... ¡hasta la próxima!")
            break
        else:
            print("Opción no válida. Inténtelo de nuevo")

# Invocar al programa principal
if __name__ == "__main__":
    main()








   