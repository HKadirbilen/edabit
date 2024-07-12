"""
Difference of Max and Min Numbers in List

Create a function that takes a list and returns the difference between the biggest and smallest numbers.

Examples
difference_max_min([10, 4, 1, 4, -10, -50, 32, 21]) ➞ 82
# Smallest number is -50, biggest is 32.

difference_max_min([44, 32, 86, 19]) ➞ 67
# Smallest number is 19, biggest is 86.
"""



from edatest import Edatest
Test = Edatest()

def difference_max_min(lst):
    return max(lst)-min(lst)

if __name__ == '__main__':
    Test.assert_equals(difference_max_min([10,4,1,2,8,91]), 90)
    Test.assert_equals(difference_max_min([-70,43,34,54,22]), 124)