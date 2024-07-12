"""
Divides Evenly

Given two integers, a and b, return True if a can be divided evenly by b. Return False otherwise.

Examples
divides_evenly(98, 7) ➞ True
# 98/7 = 14

divides_evenly(85, 4) ➞ False
# 85/4 = 21.25

Notes
a will always be greater than or equal to b.
"""



from edatest import Edatest
Test = Edatest()

def divides_evenly(a, b):
    if a % b == 0:
        return True
    else:
        return False


if __name__ == '__main__':
    Test.assert_equals(divides_evenly(98, 7), True)
    Test.assert_equals(divides_evenly(87, 49), False)
    Test.assert_equals(divides_evenly(34, 14), False)
    Test.assert_equals(divides_evenly(78, 6), True)
    Test.assert_equals(divides_evenly(30, 4), False)
    Test.assert_equals(divides_evenly(87, 73), False)
    Test.assert_equals(divides_evenly(74, 7), False)
    Test.assert_equals(divides_evenly(87, 29), True)
    Test.assert_equals(divides_evenly(48, 24), True)
    Test.assert_equals(divides_evenly(99, 20), False)
    Test.assert_equals(divides_evenly(98, 49), True)
    Test.assert_equals(divides_evenly(100, 6), False)
    Test.assert_equals(divides_evenly(64, 4), True)
    Test.assert_equals(divides_evenly(70, 35), True)
    Test.assert_equals(divides_evenly(38, 38), True)
    Test.assert_equals(divides_evenly(29, 3), False)
    Test.assert_equals(divides_evenly(20, 8), False)
    Test.assert_equals(divides_evenly(66, 50), False)
    Test.assert_equals(divides_evenly(95, 1), True)
    Test.assert_equals(divides_evenly(58, 2), True)