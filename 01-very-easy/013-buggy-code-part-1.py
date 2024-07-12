"""
Buggy Code (Part 1)

Fix the code in the code tab to pass this challenge (only syntax errors).
Look at the examples below to get an idea of what the function should do.

Examples
cubes(3) ➞ 27

cubes(5) ➞ 125

cubes(10) ➞ 1000

Notes
READ EVERY WORD CAREFULLY, CHARACTER BY CHARACTER!
Don't overthink this challenge; it's not supposed to be hard.

"""



from edatest import Edatest
Test = Edatest()

"""
def cubes(a):
	retunr a ** 3
"""

def cubes(a):
	return a ** 3

if __name__ == '__main__':
    Test.assert_equals(cubes(2), 8)
    Test.assert_equals(cubes(3), 27)
    Test.assert_equals(cubes(4), 64)
    Test.assert_equals(cubes(5), 125)
    Test.assert_equals(cubes(10), 1000)