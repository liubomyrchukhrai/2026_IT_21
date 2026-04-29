"""Test module"""

def test_example():
    """Simple test"""
    assert 1 + 1 == 2


import math
from calculator.calc import log
import pytest

def test_log_base10():
    assert log(100, 10) == 2

def test_log_natural():
    assert log(math.e, math.e) == 1

def test_log_invalid_value():
    with pytest.raises(ValueError):
        log(0)

def test_log_invalid_base():
    with pytest.raises(ValueError):
        log(10, 1)
