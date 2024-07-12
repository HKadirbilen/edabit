"""
Compare Strings by Count of Characters

Create a function that takes two strings as arguments and return either True or False depending on whether the total number of characters in the first string is equal to the total number of characters in the second string.

Examples
comp("AB", "CD") ➞ True

comp("ABC", "DE") ➞ False

comp("hello", "edabit") ➞ False

Notes
Don't forget to return the result.
If you get stuck on a challenge, find help in the Resources tab.
If you're really stuck, unlock solutions in the Solutions tab.
"""



from edatest import Edatest
Test = Edatest()

def comp(txt1, txt2):
    if len(txt1) == len(txt2):
        return True
    else:
        return False


if __name__ == '__main__':
    Test.assert_equals(comp("AB", "CD"), True)
    Test.assert_equals(comp("ABC", "DE"), False)
    Test.assert_equals(comp("hello", "edabit"), False)
    Test.assert_equals(comp("meow", "woof"), True)
    Test.assert_equals(comp("jrnvjrnnt", "cvjknfjvmfvnfjn"), False)
    Test.assert_equals(comp("jkvnjrt", "krnf"), False)
    Test.assert_equals(comp("Facebook", "Snapchat"), True)