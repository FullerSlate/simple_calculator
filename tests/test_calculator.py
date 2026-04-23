import pytest
from src.calculator.calculator import squareNums, triNums, lazyCaterer, magicSquares, hypotenuse, power, modulus

@pytest.mark.parametrize("n,expected", [
    (2, 4),
    (3, 9),
    (5, 25)
])
def test_squareNums(n, expected):
    assert squareNums(n) == expected


@pytest.mark.parametrize("n,expected", [
    (1, 1),
    (3, 6),
    (5, 15)
])
def test_triNums(n, expected):
    assert triNums(n) == expected


@pytest.mark.parametrize("n,expected", [
    (1, 2),
    (2, 4),
    (3, 7)
])
def test_lazyCaterer(n, expected):
    assert lazyCaterer(n) == expected


@pytest.mark.parametrize("n,expected", [
    (1, 1),
    (2, 5),
    (3, 15)
])
def test_magicSquares(n, expected):
    assert magicSquares(n) == expected


@pytest.mark.parametrize("a,b,expected", [
    (3, 4, 5),
    (5, 12, 13),
    (8, 15, 17)
])
def test_hypotenuse(a, b, expected):
    assert hypotenuse(a, b) == expected


@pytest.mark.parametrize("base,exp,expected", [
    (2, 3, 8),
    (5, 2, 25),
    (10, 0, 1)
])
def test_power(base, exp, expected):
    assert power(base, exp) == expected


@pytest.mark.parametrize("a,b,expected", [
    (10, 3, 1),
    (20, 5, 0),
    (7, 4, 3)
])
def test_modulus(a, b, expected):
    assert modulus(a, b) == expected