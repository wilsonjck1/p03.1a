"""
Problem:

    The function add_to_n works in exactly the same way as
    the add_100 function from the previous problem.

    However, the difference here is that it allows us to
    specify the biggest number we want to add.


Tests:

    >>> add_to_n(100)
    5050
    >>> add_to_n(500)
    125250
    >>> add_to_n(1234)
    761995

"""

# Use this to test your solution. Don't edit it!
import doctest
def run_tests():
    doctest.testmod(verbose=True)


# Edit this code
def add_to_n(n):
    total=0
    for i in range (1, n+1):
        total = total + i

    print(total)

