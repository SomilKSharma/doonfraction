import pytest

from doonfraction.doonfraction import doonfraction

def test_init():
    
    # Test that the numerator and denominator are set correctly
    f = doonfraction(3, 4)
    assert f.numerator == 3
    assert f.denominator == 4

def test_str():
    
    # Test that the string representation of the fraction is correct
    f = doonfraction(3, 4)
    assert str(f) == "3/4"

def test_add():
    
    # Test that fractions can be added
    f1 = doonfraction(1, 2)
    f2 = doonfraction(1, 4)
    f3 = f1 + f2
    assert str(f3) == "3/4"

def test_sub():
    
    # Test that fractions can be subtracted
    f1 = doonfraction(1, 2)
    f2 = doonfraction(1, 4)
    f3 = f1 - f2
    assert str(f3) == "1/4"

def test_mul():
    
    # Test that fractions can be multiplied
    f1 = doonfraction(1, 2)
    f2 = doonfraction(1, 4)
    f3 = f1 * f2
    assert str(f3) == "1/8"

def test_div():
    
    # Test that fractions can be divided
    f1 = doonfraction(1, 2)
    f2 = doonfraction(1, 4)
    f3 = f1 / f2
    assert str(f3) == "2/1"

def test_float():
    
    # Test that the fraction can be converted to a float
    f = doonfraction(1, 2)
    assert float(f) == 0.5
