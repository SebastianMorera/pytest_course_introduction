import pytest

### Chapter 8: Filtering tests

### Chapter 1: First test case
@pytest.mark.math
def test_one_plus_one():
    assert 1 + 1 == 2

### Chapter 2: Failing test case
## The error version to see a failure test case
# def test_one_plus_two():
#     a = 1
#     b = 2
#     c = 0
#     assert a + b == c

@pytest.mark.math
def test_one_plus_two():
    a = 1
    b = 2
    c = 3
    assert a + b == c

### Chapter 3: A test case with an exception
@pytest.mark.math
def test_divide_by_zero():
    with pytest.raises(ZeroDivisionError) as e:
        num = 1 / 0

    assert 'division by zero' in str(e.value)

### Chapter 4: Parametrized test cases
products = [
    (2, 3, 6),
    (1, 99, 99),
    (0, 99, 0),
    (3, -4, -12),
    (-5, -5, 25),
    (2.5, 6.7, 16.75)
]

@pytest.mark.math
@pytest.mark.parametrize('a, b, product', products)
def test_multiplication(a, b, product):
    assert a * b == product