"""
Is the Last Character an "N"?
Create a function that takes a string (a random name). If the last character of the name is an "n", return True, otherwise return False.

Examples
is_last_character_n("Aiden") ➞ True

is_last_character_n("Piet") ➞ False

is_last_character_n("Bert") ➞ False

is_last_character_n("Dean") ➞ True
Notes
The function must return a boolean value ( i.e. True or False).
"""



from edatest import Edatest
Test = Edatest()

def is_last_character_n(word):
    if word[-1] == "n":
        return True
    else:
        return False

if __name__ == '__main__':
    Test.assert_equals(is_last_character_n("Aiden"), True)
    Test.assert_equals(is_last_character_n("Roxy"), False)
    Test.assert_equals(is_last_character_n("Bert"), False)
    Test.assert_equals(is_last_character_n("Dean"), True)
    Test.assert_equals(is_last_character_n("Ian"), True)
    Test.assert_equals(is_last_character_n("Brian"), True)
    Test.assert_equals(is_last_character_n("Daniel"), False)