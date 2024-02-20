import pytest

import irsut.shapes as shapes

@pytest.fixture
def my_rectangle():
    return shapes.Rectangle(length=10, width=2)

@pytest.fixture
def weird_rectangle():
    return shapes.Rectangle(length=1,width=1)
