# proyectoBibliotecaDigital/migrar_json_a_sqlite.py
from persistence.json_manager import cargar_recursos as cargar_json
from persistence.sqlite_manager import guardar_recursos as guardar_sqlite

RUTA_JSON = "proyectoBibliotecaDigitalSQLite/data/recursos.json"
RUTA_DB   = "proyectoBibliotecaDigitalSQLite/data/recursos.db"

recursos = cargar_json(RUTA_JSON)
guardar_sqlite(RUTA_DB, recursos)

print(f"Migrados {len(recursos)} recursos a {RUTA_DB}")