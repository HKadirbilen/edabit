"""
Convert Age to Days

Create a function that takes the age in years and returns the age in days.

Examples
calc_age(65) ➞ 23725

calc_age(0) ➞ 0

calc_age(20) ➞ 7300

Notes
Use 365 days as the length of a year for this challenge.
Ignore leap years and days between last birthday and now.
Expect only positive integer inputs.

"""


from edatest import Edatest
Test = Edatest()

def calc_age(age):
    return age * 365

if __name__ == '__main__':
    Test.assert_equals(calc_age(10), 3650)
    Test.assert_equals(calc_age(0), 0)
    Test.assert_equals(calc_age(73), 26645)