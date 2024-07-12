"""
Return a String as an Integer

Create a function that takes a string and returns it as an integer.

Examples
string_int("6") ➞ 6

string_int("1000") ➞ 1000

string_int("12") ➞ 12

Notes
All numbers will be whole.
All numbers will be positive.

"""


from edatest import Edatest
Test = Edatest()

def string_int(txt):
    return int(txt) 

if __name__ == '__main__':
    Test.assert_equals(string_int("6"), 6)
    Test.assert_equals(string_int("2"), 2)
    Test.assert_equals(string_int("10"), 10)
    Test.assert_equals(string_int("666"), 666)