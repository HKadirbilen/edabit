"""
To the Power of Exponents

Create a function that takes a base number and an exponent number and returns the calculation.

Examples
calculate_exponent(5, 5) ➞ 3125

calculate_exponent(10, 10) ➞ 10000000000

calculate_exponent(3, 3) ➞ 27

Notes
All test inputs will be positive integers.
Don't forget to return the result.
If you get stuck on a challenge, find help in the Resources tab.
If you're really stuck, unlock solutions in the Solutions tab.

"""



from edatest import Edatest
Test = Edatest()

def calculate_exponent(num, exp):
    return num**exp

if __name__ == '__main__':
    Test.assert_equals(calculate_exponent(5,5), 3125)
    Test.assert_equals(calculate_exponent(3,3), 27)
    Test.assert_equals(calculate_exponent(10,10), 10000000000)