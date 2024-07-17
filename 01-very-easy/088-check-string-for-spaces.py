"""
Check String for Spaces
Create a function that returns True if a string contains any spaces.

Examples
has_spaces("hello") ➞ False

has_spaces("hello, world") ➞ True

has_spaces(" ") ➞ True

has_spaces("") ➞ False

has_spaces(",./!@#") ➞ False
Notes
An empty string does not contain any spaces.
Try doing this without RegEx.
"""



from edatest import Edatest
Test = Edatest()

def has_spaces(txt):
    if " " in txt:
        return True
    else:
        return False

if __name__ == '__main__':
    Test.assert_equals(has_spaces("Foo"), False)
    Test.assert_equals(has_spaces("Foo bar"), True)
    Test.assert_equals(has_spaces("Foo "), True)
    Test.assert_equals(has_spaces(" Foo"), True)
    Test.assert_equals(has_spaces(" "), True)
    Test.assert_equals(has_spaces(""), False)
    Test.assert_equals(has_spaces(",./;'[]-="), False)