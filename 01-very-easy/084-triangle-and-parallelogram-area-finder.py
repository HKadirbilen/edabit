"""
Triangle and Parallelogram Area Finder
Write a function that accepts base (decimal), height (decimal) and shape ("triangle", "parallelogram") as input and calculates the area of that shape.

Examples
area_shape(2, 3, "triangle") ➞ 3

area_shape(8, 6, "parallelogram") ➞ 48

area_shape(2.9, 1.3, "parallelogram") ➞ 3.77
Notes
Area of a triangle is 0.5 * b * h
Area of a parallelogram is b * h
Assume triangle and parallelogram are the only inputs for shape.
"""



from edatest import Edatest
Test = Edatest()

def area_shape(base, height, shape):
    if shape == "triangle":
        return 0.5 * base * height
    else:
        return base * height

if __name__ == '__main__':
    Test.assert_equals(area_shape(2, 3, "triangle"), 3)
    Test.assert_equals(area_shape(8, 6, "parallelogram"), 48)
    Test.assert_equals(area_shape(0, 1, "triangle"), 0)
    Test.assert_equals(area_shape(2.9, 1.3, "parallelogram"), 3.77)
    Test.assert_equals(area_shape(0.01, 5, "triangle"), 0.025)