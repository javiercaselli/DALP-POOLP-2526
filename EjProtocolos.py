from typing import Protocol


# ------------------------------
# 1. Definimos un Protocolo
# ------------------------------
class Operador(Protocol):
    def operar(self, x: float, y: float) -> float:
        ...

# ------------------------------
# 2. Varias clases que cumplen el protocolo
# ------------------------------
class Suma:
    def operar(self, x: float, y: float) -> float:
        return x + y


class Resta:
    def operar(self, x: float, y: float) -> float:
        return x - y


class Multiplicacion:
    def operar(self, x: float, y: float) -> float:
        return x * y


# ------------------------------
# 3. Clase que NO cumple el protocolo (sirve para ver error con mypy)
# ------------------------------
class MalaClase:
    def no_opera(self, x, y):
        return 0


# ------------------------------
# 4. Función que recibe cualquier Operador
# ------------------------------
def calcular(operador: Operador, a: float, b: float):
    resultado = operador.operar(a, b)
    print(f"Resultado: {resultado}")


# ------------------------------
# 5. "main" al estilo Java
# ------------------------------
def main():
    print("=== DEMOSTRACIÓN DE PROTOCOL ===")

    op1 = Suma()
    op2 = Resta()
    op3 = Multiplicacion()

    calcular(op1, 10, 5)
    calcular(op2, 10, 5)
    calcular(op3, 10, 5)

    print("\nProbando clase incorrecta...")
    try:
        calcular(MalaClase(), 10, 5)   # Esto fallará en runtime
    except AttributeError as e:
        print("ERROR:", e)


# ------------------------------
# 6. Punto de entrada del script
# ------------------------------
if __name__ == "__main__":
    main()