"""
Edaaaaabit
Write a function that takes an integer and returns a string with the given number of "a"s in Edabit.

Examples
how_many_times(5) ➞ "Edaaaaabit"

how_many_times(0) ➞ "Edbit"

how_many_times(12) ➞ "Edaaaaaaaaaaaabit"
Notes
The string must start with "Ed" and end with "bit".
You'll only be given integers as test input.
"""



from edatest import Edatest
Test = Edatest()

def how_many_times(num):
    return "Ed" + (num * "a") + "bit"

if __name__ == '__main__':
    Test.assert_equals(how_many_times(5), "Edaaaaabit")
    Test.assert_equals(how_many_times(15), "Edaaaaaaaaaaaaaaabit")
    Test.assert_equals(how_many_times(10), "Edaaaaaaaaaabit")
    Test.assert_equals(how_many_times(23), "Edaaaaaaaaaaaaaaaaaaaaaaabit")
    Test.assert_equals(how_many_times(1), "Edabit")