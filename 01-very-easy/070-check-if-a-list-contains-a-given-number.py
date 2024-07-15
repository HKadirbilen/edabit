"""
Check if a List Contains a Given Number
Write a function to check if a list contains a particular number.

Examples
check([1, 2, 3, 4, 5], 3) ➞ True

check([1, 1, 2, 1, 1], 3) ➞ False

check([5, 5, 5, 6], 5) ➞ True

check([], 5) ➞ False
Notes
Don't forget to return the result.
If you get stuck on a challenge, find help in the Resources tab.
If you're really stuck, unlock solutions in the Solutions tab.
"""



from edatest import Edatest
Test = Edatest()

def check(lst, el):
    if el in lst:
        return True
    else:
        return False

if __name__ == '__main__':
    Test.assert_equals(check([1, 2, 3, 4, 5], 3), True)
    Test.assert_equals(check([1, 1, 2, 1, 1], 3), False)
    Test.assert_equals(check([1, 1, 2, 1, 5, 4, 7], 7), True)
    Test.assert_equals(check([1, 1, 2, 1, 5, 4, 7], 8), False)
    Test.assert_equals(check([5, 5, 5, 6], 5), True)
    Test.assert_equals(check([], 5), False)