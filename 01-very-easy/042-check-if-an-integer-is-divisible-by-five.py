"""
Check if an Integer is Divisible By Five

Create a function that returns True if an integer is evenly divisible by 5, and False otherwise.

Examples
divisible_by_five(5) ➞ True

divisible_by_five(-55) ➞ True

divisible_by_five(37) ➞ False

Notes
Don't forget to return the result.
If you get stuck on a challenge, find help in the Resources tab.
If you're really stuck, unlock solutions in the Solutions tab.
"""



from edatest import Edatest
Test = Edatest()

def divisible_by_five(n):
    if n % 5 == 0:
        return True
    else:
        return False

if __name__ == '__main__':
    Test.assert_equals(divisible_by_five(7), False)
    Test.assert_equals(divisible_by_five(5), True)
    Test.assert_equals(divisible_by_five(15), True)
    Test.assert_equals(divisible_by_five(33), False)
    Test.assert_equals(divisible_by_five(-18), False)
    Test.assert_equals(divisible_by_five(999), False)
    Test.assert_equals(divisible_by_five(2), False)