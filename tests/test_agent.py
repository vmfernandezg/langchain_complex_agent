
import pytest

from agent_app.tools import (
    add,
    count_chars,
    count_words,
    divide,
    factorial,
    is_prime,
    modulus,
    multiply,
    power,
    remove_vowels,
    replace_string,
    reverse_string,
    reverse_words,
    root,
    subtract,
    to_lower,
    to_upper,
)

# --- Math Tools Tests ---


def test_add() -> None:
    assert add.invoke({"a": 5, "b": 3}) == 8
    assert add.invoke({"a": -1, "b": 1}) == 0
    assert add.invoke({"a": 0, "b": 0}) == 0


def test_subtract() -> None:
    assert subtract.invoke({"a": 10, "b": 4}) == 6
    assert subtract.invoke({"a": 5, "b": 10}) == -5


def test_multiply() -> None:
    assert multiply.invoke({"a": 6, "b": 7}) == 42
    assert multiply.invoke({"a": 5, "b": 0}) == 0
    assert multiply.invoke({"a": -2, "b": 3}) == -6


def test_divide() -> None:
    assert divide.invoke({"a": 10, "b": 2}) == 5.0
    assert divide.invoke({"a": 5, "b": 2}) == 2.5

    with pytest.raises(ValueError, match="No se puede dividir por cero."):
        divide.invoke({"a": 10, "b": 0})


def test_power() -> None:
    assert power.invoke({"a": 2, "b": 3}) == 8.0
    assert power.invoke({"a": 5, "b": 0}) == 1.0
    assert power.invoke({"a": 2, "b": -1}) == 0.5


def test_root() -> None:
    assert root.invoke({"a": 9}) == 3.0
    assert root.invoke({"a": 0}) == 0.0

    with pytest.raises(
        ValueError, match="No se puede calcular la raíz de un número negativo."
    ):
        root.invoke({"a": -4})


def test_modulus() -> None:
    assert modulus.invoke({"a": 10, "b": 3}) == 1
    assert modulus.invoke({"a": 10, "b": 5}) == 0

    with pytest.raises(ValueError, match="No se puede dividir por cero."):
        modulus.invoke({"a": 10, "b": 0})


def test_factorial() -> None:
    assert factorial.invoke({"n": 5}) == 120
    assert factorial.invoke({"n": 0}) == 1

    with pytest.raises(
        ValueError, match="No se puede calcular el factorial de un número negativo."
    ):
        factorial.invoke({"n": -1})


def test_is_prime() -> None:
    assert is_prime.invoke({"n": 7}) is True
    assert is_prime.invoke({"n": 13}) is True
    assert is_prime.invoke({"n": 4}) is False  # Composite
    assert is_prime.invoke({"n": 1}) is False  # Definition of prime > 1
    assert is_prime.invoke({"n": 0}) is False
    assert is_prime.invoke({"n": -7}) is False


# --- Text Tools Tests ---


def test_reverse_string() -> None:
    assert reverse_string.invoke({"text": "hello"}) == "olleh"
    assert reverse_string.invoke({"text": ""}) == ""
    assert reverse_string.invoke({"text": "a"}) == "a"


def test_count_chars() -> None:
    assert count_chars.invoke({"text": "hello"}) == 5
    assert count_chars.invoke({"text": "hello world"}) == 11
    assert count_chars.invoke({"text": ""}) == 0


def test_to_upper() -> None:
    assert to_upper.invoke({"text": "hello"}) == "HELLO"
    assert to_upper.invoke({"text": "MixedCase"}) == "MIXEDCASE"


def test_to_lower() -> None:
    assert to_lower.invoke({"text": "HELLO"}) == "hello"
    assert to_lower.invoke({"text": "MixedCase"}) == "mixedcase"


def test_count_words() -> None:
    assert count_words.invoke({"text": "hello world"}) == 2
    assert count_words.invoke({"text": "  hello   world  "}) == 2  # Extra spaces
    assert count_words.invoke({"text": ""}) == 0


def test_replace_string() -> None:
    assert (
        replace_string.invoke(
            {"text": "hello world", "old": "world", "new": "there"}
        )
        == "hello there"
    )
    assert replace_string.invoke({"text": "banana", "old": "a", "new": "o"}) == "bonono"


def test_reverse_words() -> None:
    assert reverse_words.invoke({"text": "hello world"}) == "world hello"
    assert reverse_words.invoke({"text": "one two three"}) == "three two one"


def test_remove_vowels() -> None:
    assert remove_vowels.invoke({"text": "hello world"}) == "hll wrld"
    assert remove_vowels.invoke({"text": "AEIOU"}) == ""
    assert remove_vowels.invoke({"text": "bcdfgh"}) == "bcdfgh"
