"""
Even or Odd?
Given a list of integers, determine whether the sum of its elements is even or odd.

The return value should be a string ("odd" or "even").

If the input list is empty, consider it as a list with a zero ([0]).

Examples
even_or_odd([0]) ➞ "even"

even_or_odd([1]) ➞ "odd"

even_or_odd([]) ➞ "even"

even_or_odd([0, 1, 5]) ➞ "even"
Notes
N/A
"""



from edatest import Edatest
Test = Edatest()

def even_or_odd(lst):
    if sum(lst) % 2 == 0:
        return "even"
    else:
        return "odd"

if __name__ == '__main__':
    Test.assert_equals(even_or_odd([0]), 'even')
    Test.assert_equals(even_or_odd([1]), 'odd')
    Test.assert_equals(even_or_odd([]), 'even')
    Test.assert_equals(even_or_odd([0, 1, 5]), 'even')
    Test.assert_equals(even_or_odd([0, 1, 3]), 'even')
    Test.assert_equals(even_or_odd([1023, 1, 2]), 'even')
    Test.assert_equals(even_or_odd([0, -1, -5]), 'even')
    Test.assert_equals(even_or_odd([0, -1, -3]), 'even')
    Test.assert_equals(even_or_odd([-1023, 1, -2]), 'even')
    Test.assert_equals(even_or_odd([0, 1, 2]), 'odd')
    Test.assert_equals(even_or_odd([0, 1, 4]), 'odd')
    Test.assert_equals(even_or_odd([1023, 1, 3]), 'odd')
    Test.assert_equals(even_or_odd([0, -1, 2]), 'odd')
    Test.assert_equals(even_or_odd([0, 1, -4]), 'odd')
    Test.assert_equals(even_or_odd([-1023, -1, 3]), 'odd')