"""
Char-to-ASCII
Create a function that returns the ASCII value of the passed in character.

Examples
ctoa("A") ➞ 65

ctoa("m") ➞ 109

ctoa("[") ➞ 91

ctoa("\") ➞ 92
Notes
Don't forget to return the result.
If you get stuck on a challenge, find help in the Resources tab.
If you're really stuck, unlock solutions in the Solutions tab.
"""



from edatest import Edatest
Test = Edatest()

def ctoa(char):
    return ord(char)

if __name__ == '__main__':
    Test.assert_equals(ctoa(' '), 32)
    Test.assert_equals(ctoa('A'), 65)
    Test.assert_equals(ctoa(']'), 93)
    Test.assert_equals(ctoa('^'), 94)
    Test.assert_equals(ctoa('c'), 99)