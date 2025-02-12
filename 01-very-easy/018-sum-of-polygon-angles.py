"""
Sum of Polygon Angles

Given an n-sided regular polygon n, return the total sum of internal angles (in degrees).

Examples
sum_polygon(3) ➞ 180

sum_polygon(4) ➞ 360

sum_polygon(6) ➞ 720

Notes
n will always be greater than 2.
The formula (n - 2) x 180 gives the sum of all the measures of the angles of an n-sided polygon.

"""



from edatest import Edatest
Test = Edatest()

def sum_polygon(n):
      return (n - 2) * 180

if __name__ == '__main__':
    from random import randint
for i in range(3, randint(50, 1000)):
	Test.assert_equals(sum_polygon(i), (i-2)*180, 'failed for n = {}'.format(i))