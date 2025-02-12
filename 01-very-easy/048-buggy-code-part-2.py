"""
Buggy Code (Part 2)

Fix the code in the code tab to pass this challenge (only syntax errors). Look at the examples below to get an idea of what the function should do.

Examples
max_num(3, 7) ➞ 7

max_num(-1, 0) ➞ 0

max_num(1000, 400) ➞ 1000

Notes
READ EVERY WORD CAREFULLY, CHARACTER BY CHARACTER!
Don't overthink this challenge; it's not supposed to be hard.
"""



from edatest import Edatest
Test = Edatest()

"""
def max_num(n1, n2):
	if n1 > n2:
		return n2
	elif:
		return n1
"""

def max_num(n1, n2):
	if n1 < n2:
		return n2
	else:
		return n1

if __name__ == '__main__':
    Test.assert_equals(max_num(3, 7), 7)
    Test.assert_equals(max_num(-1, 0), 0)
    Test.assert_equals(max_num(1000, 400), 1000)
    Test.assert_equals(max_num(-3, -9), -3)
    Test.assert_equals(max_num(88, 90), 90)