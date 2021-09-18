import pytest
from q2func import *
import numpy as np

#generating the polynomial
p = poly_solve(10,-1,1)[1] 

#initialising fixtures for use in the tests
@pytest.fixture
def input_x():
    input = x
    return input

@pytest.fixture
def input_f():
    input = f
    return input

#the test, determining whether the norm of the error is sufficiently small
@pytest.mark.print
def test_q2c(input_x, input_f):
    assert(np.linalg.norm(p(input_x) - input_f) < 1.0e-6)
    