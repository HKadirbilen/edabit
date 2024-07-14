"""
Inches to Feet
Create a function that accepts a measurement value in inches and returns the equivalent of the measurement value in feet.

Examples
inches_to_feet(324) ➞ 27

inches_to_feet(12) ➞ 1

inches_to_feet(36) ➞ 3

Notes
If inches are under 12, return 0.
12 inches = 1 foot.
"""



from edatest import Edatest
Test = Edatest()

def inches_to_feet(inches):
    return inches//12

if __name__ == '__main__':
    Test.assert_equals(inches_to_feet(12), 1) 
    Test.assert_equals(inches_to_feet(360), 30) 
    Test.assert_equals(inches_to_feet(3612), 301)
    Test.assert_equals(inches_to_feet(324), 27)
    Test.assert_equals(inches_to_feet(3012), 251)
    Test.assert_equals(inches_to_feet(11), 0)