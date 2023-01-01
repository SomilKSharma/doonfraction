# DoonFraction

A Python class for working with fractions. The `doonfraction` class allows you to create instances of fractions, perform arithmetic operations with them, and convert them to floating point numbers.

## Examples

```python
from doonfraction.doonfraction import doonfraction

# Create a fraction
f = doonfraction(3, 4)

# Perform arithmetic operations with fractions
f1 = doonfraction(1, 2)
f2 = doonfraction(1, 4)
f3 = f1 + f2
print(f3)  # prints "3/4"

f4 = f1 - f2
print(f4)  # prints "1/4"

f5 = f1 * f2
print(f5)  # prints "1/8"

f6 = f1 / f2
print(f6)  # prints "2/1"

# Convert a fraction to a float
f7 = doonfraction(1, 2)
print(float(f7))  # prints 0.5


# Convert fraction to mixed fraction
f8=doonfraction(7,2)
f9=f8.mixf()
print(f9)  #prints "3 1/2"


## 

__init__(self, num, den): Constructor to initialize the numerator and denominator.

__str__(self): Returns the string representation of the fraction in the form of "numerator/denominator".

__add__(self, other): Adds two fractions and returns the result as a new doonfraction instance.

__sub__(self, other): Subtracts two fractions and returns the result as a new doonfraction instance.

__mul__(self, other): Multiplies two fractions and returns the result as a new doonfraction instance.

__truediv__(self, other): Divides two fractions and returns the result as a new doonfraction instance.

__float__(self): Converts the fraction to a floating point number.

mixf(self): Convert a fraction to a mixed fraction

