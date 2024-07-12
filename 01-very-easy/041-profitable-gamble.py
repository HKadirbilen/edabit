"""
Profitable Gamble

Create a function that takes three arguments prob, prize, pay and returns True if prob * prize > pay; otherwise return False.

To illustrate:

profitable_gamble(0.2, 50, 9)
... should yield True, since the net profit is 1 (0.2 * 50 - 9), and 1 > 0.

Examples
profitable_gamble(0.2, 50, 9) ➞ True

profitable_gamble(0.9, 1, 2) ➞ False

profitable_gamble(0.9, 3, 2) ➞ True

Notes
A profitable gamble is a game that yields a positive net profit, 
where net profit is calculated in the following manner: net_outcome = probability_of_winning * prize - cost_of_playing.
"""



from edatest import Edatest
Test = Edatest()

def profitable_gamble(prob, prize, pay):
    if prob*prize>pay:
        return True
    else:
        return False

if __name__ == '__main__':
    Test.assert_equals(profitable_gamble(0.2, 50, 9), True)
    Test.assert_equals(profitable_gamble(0.9, 1, 2), False)
    Test.assert_equals(profitable_gamble(0.9, 3, 2), True)
    Test.assert_equals(profitable_gamble(0.33, 10, 3.30), True)
    Test.assert_equals(profitable_gamble(0, 1000, 0.01), False)
    Test.assert_equals(profitable_gamble(0.1, 1000, 7), True)
    Test.assert_equals(profitable_gamble(0, 0, 0), False)