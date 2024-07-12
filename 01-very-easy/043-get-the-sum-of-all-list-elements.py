"""
Get the Sum of All List Elements

Create a function that takes a list and returns the sum of all numbers in the list.

Examples
get_sum_of_elements([2, 7, 4]) ➞ 13

get_sum_of_elements([45, 3, 0]) ➞ 48

get_sum_of_elements([-2, 84, 23]) ➞ 105
"""

from edatest import Edatest
Test = Edatest()

def get_sum_of_elements(lst):
    return sum(lst)

if __name__ == '__main__':
    Test.assert_equals(get_sum_of_elements([2, 7, 4]), 13)
    Test.assert_equals(get_sum_of_elements([45, 3, 0]), 48)
    Test.assert_equals(get_sum_of_elements([-2, 84, 23]), 105)
