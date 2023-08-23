import pytest
from src.main import sum, login, cambio, holaMundo, numPI, countLengt, numPrimos, genFibonacci
# python -m pytest -v

@pytest.mark.parametrize(
    "input_x, input_y, expected",
    [
        (5, 1, 6),
        (6, 4, 10),
        (5, 4, 9),
        (5, sum(10, 2), 17)
    ]
)
def test_sum_params(input_x, input_y, expected):
    assert sum(input_x,input_y) == expected


def test_login_pass():
    login_pass = login("username", "password")
    assert login_pass


def test_login_fail():
    login_pass = login("username1", "password")
    assert not login_pass


@pytest.mark.parametrize(
    "input_x, input_y, expected",
    [
        (5, 1, 4),
        (4, 5, -1),
        (2, 10, -8),
        (5, 5, 0)
    ]
)
def test_cambio_params_pass(input_x, input_y, expected):
    assert cambio(input_x, input_y) == expected


def test_cambio_params_fail():
    assert not cambio(5, 5) == 1


def test_holaMundo():
    assert holaMundo() == "¡Hola, mundo!"


@pytest.mark.parametrize(
    "input_x, input_y, expected",
    [
        (1, 10, [[1,3,5,7,9], [2,4,6,8,10]]),
        (1, 4, [[1,3], [2,4]])
    ]
)
def test_numIP(input_x, input_y, expected):
    assert numPI(input_x, input_y) == expected


@pytest.mark.parametrize(
    "input_x, expected",
    [
        ("Hola que tal.", 3),
        ("Hola.", 1)
    ]
)
def test_count(input_x, expected):
    assert countLengt(input_x) == expected


@pytest.mark.parametrize(
    "input_x, expected",
    [
        (11, True),
        (8, False),
        (1, False)
    ]
)
def test_numPrimos(input_x, expected):
    assert numPrimos(input_x) == expected


def test_fibonacci():
    assert genFibonacci(10) == [0, 1, 1, 2, 3, 5, 8, 13, 21, 34]
