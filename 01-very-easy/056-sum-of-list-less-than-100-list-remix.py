"""
Sum of List Less Than 100 List Remix

Given a list of numbers, return True if the sum of the values in the list is less than 100; otherwise return False.

Examples
list_less_than_100([5, 57]) ➞ True

list_less_than_100([77, 30]) ➞ False

list_less_than_100([0]) ➞ True
"""



from edatest import Edatest
Test = Edatest()

def list_less_than_100(lst):
    if sum(lst) < 100:
        return True
    else:
        return False

if __name__ == '__main__':
    Test.assert_equals(list_less_than_100([5, 57]), True)
    Test.assert_equals(list_less_than_100([77, 30]), False)
    Test.assert_equals(list_less_than_100([0, 59,15]), True)
    Test.assert_equals(list_less_than_100([0]), True)
    Test.assert_equals(list_less_than_100([35, 59,15]), False)
    Test.assert_equals(list_less_than_100([25, 50, 25]), False)