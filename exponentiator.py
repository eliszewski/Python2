import math
"""
Take 2 numbers and raised first to the power of second
"""

def exponentiate(base,power):
    return base**power
"""
raises a number to the 4th power
"""
def raise_to_the_fourth_power(base):
    return exponentiate(base,4)

square = lambda base: exponentiate(base,2)
cube = lambda base: exponentiate(base,3)
print(square(2))
print(cube(2))
print(raise_to_the_fourth_power(2))
