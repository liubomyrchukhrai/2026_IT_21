"""Test module calculator"""

import pytest
from calculator import square

def test_example():
    """Simple test"""
    assert 1 + 1 == 2

def test_square():
    """Test square function"""
    assert square(2,2) == 4
    assert square(3,2) == 9
