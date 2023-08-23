import pytest
from src.main import sum, login, cambio


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