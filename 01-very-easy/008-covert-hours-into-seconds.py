"""
Convert Hours into Seconds

Write a function that converts hours into seconds.

Examples
how_many_seconds(2) ➞ 7200

how_many_seconds(10) ➞ 36000

how_many_seconds(24) ➞ 86400
Notes
60 seconds in a minute, 60 minutes in an hour
Don't forget to return your answer.

"""



from edatest import Edatest
Test = Edatest()

def how_many_seconds(hours):
    return hours * 3600


if __name__ == '__main__':
    Test.assert_equals(how_many_seconds(2), 7200)
    Test.assert_equals(how_many_seconds(10), 36000)
    Test.assert_equals(how_many_seconds(24), 86400)
    Test.assert_equals(how_many_seconds(36), 129600)