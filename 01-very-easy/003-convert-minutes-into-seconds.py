"""
Convert Minutes into Seconds

Write a function that takes an integer minutes and converts it to seconds.

Examples
convert(5) ➞ 300

convert(3) ➞ 180

convert(2) ➞ 120

Notes
Don't forget to return the result.
If you get stuck on a challenge, find help in the Resources tab.
If you're really stuck, unlock solutions in the Solutions tab.

"""


from edatest import Edatest
Test = Edatest()

def convert(minutes):
    return minutes * 60 

if __name__ == '__main__':
    Test.assert_equals(convert(6), 360)
    Test.assert_equals(convert(4), 240)
    Test.assert_equals(convert(8), 480)
    Test.assert_equals(convert(60), 3600)