"""
Fix the Error: Check Whether a Given Number Is Odd
Éowyn has written the function is_odd() to check if a given number is odd or not. Unfortunately, the function does not return the correct result for all the inputs. Help her fix the error.

def is_odd(num):
  return num % 1 == 1 or 2
Examples
is_odd(-5) ➞ True

is_odd(25) ➞ True

is_odd(0) ➞ False
Notes
All the inputs will only be integers.
"""



from edatest import Edatest
Test = Edatest()

"""
def is_odd(num):
  return num % 1 == 1 or 2
"""

def is_odd(num):
  return num % 2 > 0

if __name__ == '__main__':
    Test.assert_equals(is_odd(-5), True)
    Test.assert_equals(is_odd(-50), False)
    Test.assert_equals(is_odd(0), False)
    Test.assert_equals(is_odd(25), True)
    Test.assert_equals(is_odd(-19), True)
    Test.assert_equals(is_odd(12), False)
    Test.assert_equals(is_odd(23), True)
    Test.assert_equals(is_odd(-71), True)