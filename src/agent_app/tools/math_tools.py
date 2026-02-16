from langchain_core.tools import tool


@tool
def add(a: int, b: int) -> int:
    """Suma dos enteros."""
    return a + b


@tool
def multiply(a: int, b: int) -> int:
    """Multiplica dos enteros."""
    return a * b


@tool
def subtract(a: int, b: int) -> int:
    """Resta el segundo entero del primero."""
    return a - b


@tool
def divide(a: int, b: int) -> float:
    """Divide el primer entero por el segundo."""
    if b == 0:
        raise ValueError("No se puede dividir por cero.")
    return a / b


@tool
def power(a: int, b: int) -> float:
    """Eleva el primer entero a la potencia del segundo."""
    return a ** b


@tool
def root(a: int) -> float:
    """Calcula la raíz cuadrada del entero."""
    if a < 0:
        raise ValueError("No se puede calcular la raíz de un número negativo.")
    return a ** 0.5


@tool
def modulus(a: int, b: int) -> int:
    """Calcula el módulo (resto) de la división de a por b."""
    if b == 0:
        raise ValueError("No se puede dividir por cero.")
    return a % b


@tool
def factorial(n: int) -> int:
    """Calcula el factorial de un entero no negativo."""
    if n < 0:
        raise ValueError("No se puede calcular el factorial de un número negativo.")
    if n == 0:
        return 1
    result = 1
    for i in range(1, n + 1):
        result *= i
    return result


@tool
def is_prime(n: int) -> bool:
    """Comprueba si un número es primo."""
    if n <= 1:
        return False
    for i in range(2, int(n**0.5) + 1):
        if n % i == 0:
            return False
    return True
