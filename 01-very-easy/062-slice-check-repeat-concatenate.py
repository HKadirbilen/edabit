"""
Slice Check Repeat Concatenate

Create a function that takes a string; we'll say that the front is the first three characters of the string. If the string length is less than three characters, the front is whatever is there. Return a new string, which is three copies of the front.

Examples
front3("Python") ➞ "PytPytPyt"

front3("Cucumber") ➞ "CucCucCuc"

front3("bioshock") ➞ "biobiobio"

front3("Z") ➞ "ZZZ"

Notes
Don't forget to return the result.
"""



from edatest import Edatest
Test = Edatest()

def front3(txt):
    return txt[0:3] * 3

if __name__ == '__main__':
    Test.assert_equals(front3('Python'), 'PytPytPyt', 'Simple string#1')	
    Test.assert_equals(front3('Chocolate'), 'ChoChoCho', 'Simple strin#2')	
    Test.assert_equals(front3('duh'), 'duhduhduh', '3 characters string')	
    Test.assert_equals(front3('Sportsmanship'), 'SpoSpoSpo', 'Generic string')	
    Test.assert_equals(front3('ab'), 'ababab', '2 characters string')
    Test.assert_equals(front3('a'), 'aaa', '1 characters string')	
    Test.assert_equals(front3(''), '', 'Empty string')