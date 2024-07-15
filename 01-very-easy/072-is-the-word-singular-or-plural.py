"""
Is the Word Singular or Plural?
Create a function that takes in a word and determines whether or not it is plural. A plural word is one that ends in "s".

Examples
is_plural("changes") ➞ True

is_plural("change") ➞ False

is_plural("dudes") ➞ True

is_plural("magic") ➞ False
Notes
Don't forget to return the result.
Remember that return True (boolean) is not the same as return "True" (string).
This is an oversimplification of the English language. We are ignoring edge cases like "goose" and "geese", "fungus" and "fungi", etc.
If you get stuck on a challenge, find help in the Resources tab.
If you're really stuck, unlock solutions in the Solutions tab.
"""



from edatest import Edatest
Test = Edatest()

def is_plural(word):
    if  word[-1] == "s":
        return True
    else:
        return False

if __name__ == '__main__':
    Test.assert_equals(is_plural("dudes"), True)
    Test.assert_equals(is_plural("flowers"), True)
    Test.assert_equals(is_plural("checks"), True)
    Test.assert_equals(is_plural("varies"), True)
    Test.assert_equals(is_plural("efforts"), True)
    Test.assert_equals(is_plural("mood"), False)
    Test.assert_equals(is_plural("whiteboard"), False)
    Test.assert_equals(is_plural("cow"), False)
    Test.assert_equals(is_plural("word"), False)
    Test.assert_equals(is_plural("love"), False)
    Test.assert_equals(is_plural("silly"), False)