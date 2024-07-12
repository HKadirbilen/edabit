"""
Area of a Triangle

Write a function that takes the base and height of a triangle and return its area.

Examples
tri_area(3, 2) ➞ 3

tri_area(7, 4) ➞ 14

tri_area(10, 10) ➞ 50

Notes
The area of a triangle is: (base * height) / 2
Don't forget to return the result.
If you get stuck on a challenge, find help in the Resources tab.
If you're really stuck, unlock solutions in the Solutions tab.

"""



from edatest import Edatest
Test = Edatest()

def tri_area(base, height):
    return (base * height) / 2

if __name__ == '__main__':
    Test.assert_equals(tri_area(3, 2), 3)
    Test.assert_equals(tri_area(5, 4), 10)
    Test.assert_equals(tri_area(10, 10), 50)
    Test.assert_equals(tri_area(0, 60), 0)
    Test.assert_equals(tri_area(12, 11), 66)