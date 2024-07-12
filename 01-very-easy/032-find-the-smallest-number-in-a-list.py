"""
Find the Smallest Number in a List

Create a function that takes a list of numbers and returns the smallest number in the list.

Examples
find_smallest_num([34, 15, 88, 2]) ➞ 2

find_smallest_num([34, -345, -1, 100]) ➞ -345

find_smallest_num([-76, 1.345, 1, 0]) ➞ -76

find_smallest_num([0.4356, 0.8795, 0.5435, -0.9999]) ➞ -0.9999

find_smallest_num([7, 7, 7]) ➞ 7

Notes
Test cases contain decimals.
If you get stuck on a challenge, find help in the Resources tab.
If you're really stuck, unlock solutions in the Solutions tab.
"""



from edatest import Edatest
Test = Edatest()

def find_smallest_num(lst):
    return min(lst)

if __name__ == '__main__':
    Test.assert_equals(find_smallest_num([34, 15, 88, 2]), 2)
    Test.assert_equals(find_smallest_num([34, -345, -1, 100]), -345)
    Test.assert_equals(find_smallest_num([-76, 1.345, 1, 0]), -76)
    Test.assert_equals(find_smallest_num([0.4356, 0.8795, 0.5435, -0.9999]), -0.9999)
    Test.assert_equals(find_smallest_num([7, 7, 7]), 7)
    Test.assert_equals(find_smallest_num([4, 6, 1, 3, 4, 5, 5, 1]), 1)
    Test.assert_equals(find_smallest_num([-4, -6, -8, -1]), -8)
    Test.assert_equals(find_smallest_num([54, 76, 23, 54]), 23)
    Test.assert_equals(find_smallest_num([100]), 100)
    Test.assert_equals(find_smallest_num([0, 1, 2, 3, 4, 5]), 0)