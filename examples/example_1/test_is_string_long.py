from examples.example_1.is_string_long import is_string_long


def test_is_string_long() -> None:
    result = is_string_long("Hello friends")

    assert result == True


def test_is_string_short() -> None:
    result = is_string_long("Hi")

    assert result == False
