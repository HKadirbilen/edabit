"""
Return the Remainder from Two Numbers

There is a single operator in Python, capable of providing the remainder of a division operation. 
Two numbers are passed as parameters. 
The first parameter divided by the second parameter will have a remainder, possibly zero. Return that value.

Examples
remainder(1, 3) ➞ 1

remainder(3, 4) ➞ 3

remainder(5, 5) ➞ 0

remainder(7, 2) ➞ 1

Notes
The tests only use positive integers.
Don't forget to return the result.
If you get stuck on a challenge, find help in the Resources tab.

"""


from edatest import Edatest
Test = Edatest()

def remainder(x, y):
    return x % y

if __name__ == '__main__':
    Test.assert_equals(remainder(7, 2), 1)
    Test.assert_equals(remainder(3, 4), 3)
    Test.assert_equals(remainder(5, 5), 0)
    Test.assert_equals(remainder(1, 3), 1)