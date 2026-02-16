from langchain_core.tools import tool


@tool
def reverse_string(text: str) -> str:
    """Invierte la cadena de texto (e.g. 'abc' -> 'cba')."""
    return text[::-1]


@tool
def count_chars(text: str) -> int:
    """Cuenta el número de caracteres en la cadena."""
    return len(text)


@tool
def to_upper(text: str) -> str:
    """Convierte la cadena a mayúsculas."""
    return text.upper()


@tool
def to_lower(text: str) -> str:
    """Convierte la cadena a minúsculas."""
    return text.lower()


@tool
def count_words(text: str) -> int:
    """Cuenta el número de palabras en la cadena."""
    return len(text.split())


@tool
def replace_string(text: str, old: str, new: str) -> str:
    """Reemplaza ocurrencias de una subcadena con una nueva cadena."""
    return text.replace(old, new)


@tool
def reverse_words(text: str) -> str:
    """Invierte el orden de las palabras en la cadena."""
    return " ".join(text.split()[::-1])


@tool
def remove_vowels(text: str) -> str:
    """Elimina todas las vocales de la cadena."""
    vowels = "aeiouAEIOU"
    return "".join([char for char in text if char not in vowels])
