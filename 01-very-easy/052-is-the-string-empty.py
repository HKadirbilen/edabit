"""
Is the String Empty?

Create a function that returns True if a string is empty and False otherwise.

Examples
is_empty("") ➞ True

is_empty(" ") ➞ False

is_empty("a") ➞ False

Notes
A string containing only whitespaces " " does not count as empty.
Don't forget to return the result.
If you get stuck on a challenge, find help in the Resources tab.
If you're really stuck, unlock solutions in the Solutions tab.
"""



from edatest import Edatest
Test = Edatest()

def is_empty(s):
    if len(s) == 0:
        return True
    else:
        return False

if __name__ == '__main__':
    Test.assert_equals(is_empty(""), True)
    Test.assert_equals(is_empty(" "), False)
    Test.assert_equals(is_empty("            "), False)
    Test.assert_equals(is_empty("38215"), False)
    Test.assert_equals(is_empty("afjabsdf"), False)
    Test.assert_equals(is_empty("!?@&"), False)