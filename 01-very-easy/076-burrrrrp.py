"""
Burrrrrrrp
Create a function that returns the string "Burp" with the amount of "r's" determined by the input parameters of the function.

Examples
long_burp(3) ➞ "Burrrp"

long_burp(5) ➞ "Burrrrrp"

long_burp(9) ➞ "Burrrrrrrrrp"
Notes
Expect num to always be >= 1.
Remember to use a capital "B".
Don't forget to return the result.
"""



from edatest import Edatest
Test = Edatest()

def long_burp(num):
    return "Bu" + (num * "r") + "p"


if __name__ == '__main__':
    Test.assert_equals(long_burp(3), "Burrrp")
    Test.assert_equals(long_burp(5), "Burrrrrp")
    Test.assert_equals(long_burp(9), "Burrrrrrrrrp")
    Test.assert_equals(long_burp(10), "Burrrrrrrrrrp")
    Test.assert_equals(long_burp(13), "Burrrrrrrrrrrrrp")
    Test.assert_equals(long_burp(18), "Burrrrrrrrrrrrrrrrrrp")
    Test.assert_equals(long_burp(1), "Burp")