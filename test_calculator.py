import pytest  # type: ignore

from src.calculator import add, subtract, division
from src.user_input import get_user_input_and_double, get_user_inputs_and_add

def test_basic():
    assert "hello" == "hello"

def test_add():
    assert add(1,2) == 3
    assert add (-5, -2) == -7

def test_subract():
    assert subtract(8, 3) == 5
    assert subtract(-6, 2) == -8


@pytest.mark.parametrize("input1, input2, expected", 
                            [
                                (8, 3, 5),
                                (-6, 2, -8),
                                (10, 7, 3),
                                (244, 120, 124)
                            ])
def test_subtract_parameter(input1, input2, expected):
    assert subtract(input1, input2) == expected

def test_division():
    with pytest.raises(Exception):
        division(5, 0)

def test_user_input_double(monkeypatch):
    monkeypatch.setattr("builtins.input", lambda _: "6")
    result = get_user_input_and_double()
    assert result == 12

def test_user_inputs_add(monkeypatch):
    inputs = iter(["5", "6"])
    monkeypatch.setattr("builtins.input", lambda _: next(inputs))
    sum = get_user_inputs_and_add()
    assert sum == 11    