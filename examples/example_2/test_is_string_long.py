from examples.example_2.is_string_long import IsStringLong


def test_is_string_long() -> None:
    string_checker = IsStringLong()
    result = string_checker.is_long("Hello friends")

    assert True == string_checker.last_string_long
    assert True == result

    result = string_checker.is_long("Hi")

    assert False == string_checker.last_string_long
    assert False == result


def test_is_string_short() -> None:
    string_checker = IsStringLong()
    result = string_checker.is_long("Hi")

    assert False == result
