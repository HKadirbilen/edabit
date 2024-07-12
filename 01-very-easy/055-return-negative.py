"""
Return Negative

Create a function that takes a number as an argument and returns negative of that number. Return negative numbers without any change.

Examples
return_negative(4) ➞ -4

return_negative(15) ➞ -15

return_negative(-4) ➞ -4

return_negative(0) ➞ 0
"""



from edatest import Edatest
Test = Edatest()

def return_negative(n):
    if n > 0:
        return n * -1
    else:
        return n
    
if __name__ == '__main__':
    Test.assert_equals(return_negative(4), -4)
    Test.assert_equals(return_negative(15), -15)
    Test.assert_equals(return_negative(-4), -4)
    Test.assert_equals(return_negative(42), -42)
    Test.assert_equals(return_negative(-9), -9)
    Test.assert_equals(return_negative(0), 0)
    Test.assert_equals(return_negative(1), -1)
    Test.assert_equals(return_negative(-1), -1)