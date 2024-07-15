"""
Is the Number Even or Odd?
Create a function that takes a number as an argument and returns "even" for even numbers and "odd" for odd numbers.

Examples
isEvenOrOdd(3) ➞ "odd"

isEvenOrOdd(146) ➞ "even"

isEvenOrOdd(19) ➞ "odd"
Notes
Dont forget to return the result.
Input will always be a valid integer.
Expect negative integers (whole numbers).
Tests are case sensitive (return "even" or "odd" in lowercase).
"""



from edatest import Edatest
Test = Edatest()

def isEvenOrOdd(num):
    if num % 2 == 0:
        return "even"
    else:
        return "odd"
    
if __name__ == '__main__':
    Test.assert_equals(isEvenOrOdd(3), "odd")
    Test.assert_equals(isEvenOrOdd(0), "even")
    Test.assert_equals(isEvenOrOdd(7), "odd")
    Test.assert_equals(isEvenOrOdd(12), "even")
    Test.assert_equals(isEvenOrOdd(6474), "even")
    Test.assert_equals(isEvenOrOdd(3), "odd")
    Test.assert_equals(isEvenOrOdd(301), "odd")
    Test.assert_equals(isEvenOrOdd(-3), "odd")
    Test.assert_equals(isEvenOrOdd(-0), "even")
    Test.assert_equals(isEvenOrOdd(-7), "odd")
    Test.assert_equals(isEvenOrOdd(-12), "even")
    Test.assert_equals(isEvenOrOdd(-6474), "even")
    Test.assert_equals(isEvenOrOdd(-3), "odd")
    Test.assert_equals(isEvenOrOdd(-301), "odd")