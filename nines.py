"""
Problem:

    The function print_nines should print the nine times
    table, from 9 to 63.

    The function already works, but the implementation
    is shoddy. Rewrite the code using a loop.

Test:

    >>> print_nines()
    1 x 9 = 9
    2 x 9 = 18
    3 x 9 = 27
    4 x 9 = 36
    5 x 9 = 45
    6 x 9 = 54
    7 x 9 = 63

"""

# Use this to test your solution. Don't edit it!
import doctest
def run_tests():
    doctest.testmod(verbose=True)


# Edit this code
def print_nines():

    print(1, "x 9 =", 1*9)
    print(2, "x 9 =", 2*9)
    print(3, "x 9 =", 3*9)
    print(4, "x 9 =", 4*9)
    print(5, "x 9 =", 5*9)
    print(6, "x 9 =", 6*9)
    print(7, "x 9 =", 7*9)
