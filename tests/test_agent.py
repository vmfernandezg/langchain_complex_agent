from agent_app.tools import add, count_chars, multiply, reverse_string


def test_math_tools() -> None:
    """Tests the math tools."""
    assert add.invoke({"a": 5, "b": 3}) == 8
    assert multiply.invoke({"a": 10, "b": 2}) == 20


def test_text_tools() -> None:
    """Tests the text tools."""
    assert reverse_string.invoke({"text": "hello"}) == "olleh"
    assert count_chars.invoke({"text": "hello"}) == 5
