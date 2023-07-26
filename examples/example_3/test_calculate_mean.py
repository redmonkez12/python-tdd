from examples.example_3.calculate_mean import calculate_mean


def test_calculate_mean() -> None:
    result = calculate_mean([1, 2, 3, 4])
    assert 2.5 == result


def test_calculate_mean_empty_list() -> None:
    result = calculate_mean([])
    assert 0 == result