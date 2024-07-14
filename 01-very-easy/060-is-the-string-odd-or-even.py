"""
Is the String Odd or Even?

Given a string, return True if its length is even or False if the length is odd.

Examples
odd_or_even("apples") ➞ True
# The word "apples" has 6 characters.
# 6 is an even number, so the program outputs True.

odd_or_even("pears") ➞ False
# "pears" has 5 letters, and 5 is odd.
# Therefore the program outputs False.

odd_or_even("cherry") ➞ True
"""



from edatest import Edatest
Test = Edatest()

def odd_or_even(word):
    if len(word) % 2 == 0:
        return True
    else:
        return False

if __name__ == '__main__':
    Test.assert_equals(odd_or_even("apples"), True)
    Test.assert_equals(odd_or_even("banana"), True)
    Test.assert_equals(odd_or_even("cherry"), True)
    Test.assert_equals(odd_or_even("mango"), False)
    Test.assert_equals(odd_or_even("peach"), False)
    Test.assert_equals(odd_or_even("pears"), False)