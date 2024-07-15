"""
Flip the Boolean
Due to a programming concept known as truthiness, certain values can be evaluated to (i.e. take the place of) booleans.
For example, 1 (or any number other than 0) is often equivalent to True, and 0 is often equivalent to False.

Create a function that returns the opposite of the given boolean, as a number.

Examples
flip_bool(True) ➞ 0

flip_bool(False) ➞ 1

flip_bool(1) ➞ 0

flip_bool(0) ➞ 1
"""



from edatest import Edatest
Test = Edatest()

def flip_bool(b):
    if bool(b) == False:
        return 1
    else:
        return 0

if __name__ == '__main__':
    Test.assert_equals(flip_bool(1), 0)
    Test.assert_equals(flip_bool(True), 0)
    Test.assert_equals(flip_bool(0), 1)
    Test.assert_equals(flip_bool(False), 1)