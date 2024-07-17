"""
Word without First Character
Create a function that takes a word and returns the new word without including the first character.

Examples
new_word("apple") ➞ "pple"

new_word("cherry") ➞ "herry"

new_word("plum") ➞ "lum"
Notes
The input is always a valid word.
"""



from edatest import Edatest
Test = Edatest()

def new_word(word):
    return word[1:]

if __name__ == '__main__':
    Test.assert_equals(new_word("pokhara"), "okhara")
    Test.assert_equals(new_word("biratnagar"), "iratnagar")
    Test.assert_equals(new_word("nepal"), "epal")
    Test.assert_equals(new_word("damak"), "amak")
    Test.assert_equals(new_word("itahari"), "tahari")
    Test.assert_equals(new_word("rasuwa"), "asuwa")
    Test.assert_equals(new_word("rolpa"), "olpa")