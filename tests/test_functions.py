import pytest
import time
import irsut.functions as functions


def test_add():
    result = functions.add(a=1, b=8)
    assert result == 9


def test_add_string():
    result = functions.add('a', 'b')
    assert result == 'ab'


def test_sub():
    assert functions.sub(a=10, b=2) == 8


def test_divide():
    assert functions.divide(a=10, b=2) == 5


def test_divide_by_zero():
    with pytest.raises(ValueError):
        functions.divide(a=10, b=0)

@pytest.mark.slow
def test_very_slow():
    time.sleep(1)
    assert functions.divide(a=10, b=2) == 5

@pytest.mark.skip(reason="broken")
def test_add_2():
    result = functions.add(a=1, b=8)
    assert result == 8

@pytest.mark.xfail(reason='divide by zerp')
def test_divide_by_zero_broken():
    functions.divide(a=10, b=0)