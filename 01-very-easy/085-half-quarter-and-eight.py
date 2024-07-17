"""
Half, Quarter and Eighth
Create a function that takes a number and return a list of three numbers: half of the number, quarter of the number and an eighth of the number.

Examples
half_quarter_eighth(6) ➞ [3, 1.5, 0.75]

half_quarter_eighth(22) ➞ [11, 5.5, 2.75]

half_quarter_eighth(25) ➞ [12.5, 6.25, 3.125]
Notes
The order of the list is: half, quarter, eighth.
"""



from edatest import Edatest
Test = Edatest()

def half_quarter_eighth(n):
    return [n / 2, n / 4, n / 8]

if __name__ == '__main__':
    Test.assert_equals(half_quarter_eighth(6), [3, 1.5, 0.75])
    Test.assert_equals(half_quarter_eighth(22), [11, 5.5, 2.75])
    Test.assert_equals(half_quarter_eighth(25), [12.5, 6.25, 3.125])
    Test.assert_equals(half_quarter_eighth(18), [9, 4.5, 2.25])
    Test.assert_equals(half_quarter_eighth(98), [49, 24.5, 12.25])
    Test.assert_equals(half_quarter_eighth(14), [7, 3.5, 1.75])