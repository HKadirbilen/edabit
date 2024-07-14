"""
Concatenating First and Last Character of a String

Create a function that takes a string and returns the concatenated first and last character.

Examples
first_last("ganesh") ➞ "gh"

first_last("kali") ➞ "ki"

first_last("shiva") ➞ "sa"

first_last("vishnu") ➞ "vu"

first_last("durga") ➞ "da"

Notes
There is no empty string.
"""



from edatest import Edatest
Test = Edatest()

def first_last(name):
    return name[0] + name[-1]

if __name__ == '__main__':
    Test.assert_equals(first_last("ganesh"), "gh")
    Test.assert_equals(first_last("kali"), "ki")
    Test.assert_equals(first_last("shiva"), "sa")
    Test.assert_equals(first_last("vishnu"), "vu")
    Test.assert_equals(first_last("durga"), "da")
    Test.assert_equals(first_last("brahma"), "ba")