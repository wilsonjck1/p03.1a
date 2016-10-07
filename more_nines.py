"""
Problem:

    The function print_nines takes an input, n, and should
    then print the first n terms in the 9 times table,
    exactly as in the nines problem.

Test:

    >>> print_nines(2)
    1 x 9 = 9
    2 x 9 = 18
    >>> print_nines(7)
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
def print_nines(n):

   for i in range(1, n+1):
       print( i, "x 9 =", i*9)
