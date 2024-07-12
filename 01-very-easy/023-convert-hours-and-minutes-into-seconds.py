"""
Convert Hours and Minutes into Seconds

Write a function that takes two integers (hours, minutes), converts them to seconds, and adds them.

Examples
convert(1, 3) ➞ 3780

convert(2, 0) ➞ 7200

convert(0, 0) ➞ 0

Notes
Don't forget to return the result.
If you get stuck on a challenge, find help in the Resources tab.
If you're really stuck, unlock solutions in the Solutions tab.

"""


from edatest import Edatest
Test = Edatest()

def convert(hours, minutes):
    return (hours*3600)+(minutes*60)

if __name__ == '__main__':
    Test.assert_equals(convert(1, 0), 3600)
    Test.assert_equals(convert(1, 3), 3780)
    Test.assert_equals(convert(0, 30), 1800)