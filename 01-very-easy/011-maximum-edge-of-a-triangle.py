"""
Maximum Edge of a Triangle

Create a function that finds the maximum range of a triangle's third edge, where the side lengths are all integers.

Examples
next_edge(8, 10) ➞ 17

next_edge(5, 7) ➞ 11

next_edge(9, 2) ➞ 10

Notes
(side1 + side2) - 1 = maximum range of third edge.
The side lengths of the triangle are positive integers.
Don't forget to return the result.
"""



from edatest import Edatest
Test = Edatest()

def next_edge(side1, side2):
    return (side1 + side2) - 1

if __name__ == '__main__':
    Test.assert_equals(next_edge(5, 4), 8)
    Test.assert_equals(next_edge(8, 3), 10)
    Test.assert_equals(next_edge(7, 9), 15)
    Test.assert_equals(next_edge(10, 4), 13)
    Test.assert_equals(next_edge(7, 2), 8)