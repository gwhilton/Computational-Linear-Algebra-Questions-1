import pytest
from q4func import *
import numpy as np

#obtaining the polynomials
p1 = rock_solve(13)[0]
p2 = rock_solve(13)[1]

#initialising fixtures for use in the tests
@pytest.fixture
def input_x1():
    input = z[:50]
    return input

@pytest.fixture
def input_y1():
    input = Y[:50]
    return input

@pytest.fixture
def input_x2():
    input = z[50:]
    return input

@pytest.fixture
def input_y2():
    input = Y[50:]
    return input

@pytest.fixture
def input_x3():
    input = np.concatenate((p1(z[:50]),p2(z[50:])),axis=0)
    return input

@pytest.fixture
def input_y3():
    input = Y
    return input

#our tests, comparing the norm of the error vectors
@pytest.mark.print
def test_p1(input_x1, input_y1):
    assert(np.linalg.norm(p1(input_x1) - input_y1) < 1.5)

@pytest.mark.print
def test_p2(input_x2, input_y2):
    assert(np.linalg.norm(p2(input_x2) - input_y2) < 1.5)

@pytest.mark.print
def test_p(input_x3, input_y3):
    assert(np.linalg.norm(input_x3 - input_y3) < 2)