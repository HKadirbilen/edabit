"""
Concatenate First and Last Name into One String

Given two strings, first_name and last_name, return a single string in the format "last, first".

Examples
concat_name("First", "Last") ➞ "Last, First"

concat_name("John", "Doe") ➞ "Doe, John"

concat_name("Mary", "Jane") ➞ "Jane, Mary"

Notes
Don't forget to return the result.
If you get stuck on a challenge, find help in the Resources tab.
If you're really stuck, unlock solutions in the Solutions tab.
"""



from edatest import Edatest
Test = Edatest()

def concat_name(first_name, last_name):
    return last_name + ", " + first_name

if __name__ == '__main__':
    Test.assert_equals(concat_name("John", "Doe"), "Doe, John")
    Test.assert_equals(concat_name("First", "Last"), "Last, First")
    Test.assert_equals(concat_name("A", "B"), "B, A")
    Test.assert_equals(concat_name(",", ","), ",, ,")