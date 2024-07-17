"""
Find the Smallest and Biggest Numbers
Create a function that accepts a list of numbers and return both the minimum and maximum numbers, in that order (as a list).

Examples
min_max([1, 2, 3, 4, 5]) ➞ [1, 5]

min_max([2334454, 5]) ➞ [5, 2334454]

min_max([1]) ➞ [1, 1]
Notes
All test lists will have at least one element and are valid.
"""



from edatest import Edatest
Test = Edatest()

def min_max(nums):
    return [min(nums), max(nums)]

if __name__ == '__main__':
    Test.assert_equals(min_max([14, 35, 6, 1, 34, 54]), [1, 54])
    Test.assert_equals(min_max([1.346, 1.6532, 1.8734, 1.8723]), [1.346, 1.8734])
    Test.assert_equals(min_max([0.432, 0.874, 0.523, 0.984, 0.327, 0.2345]), [0.2345, 0.984])
    Test.assert_equals(min_max([13, 72, 98, 43, 24, 65, 31]), [13, 98])
    Test.assert_equals(min_max([-54, -23, -54, -21]), [-54, -21])
    Test.assert_equals(min_max([-0.473, -0.6834, -0.1287, 0.5632]), [-0.6834, 0.5632])
    Test.assert_equals(min_max([0, 0, 0, 0]), [0, 0])