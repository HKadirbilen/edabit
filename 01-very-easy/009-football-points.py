"""
Football Points

Create a function that takes the number of wins, draws and losses and calculates the number of points a football team has obtained so far.

wins get 3 points
draws get 1 point
losses get 0 points

Examples
football_points(3, 4, 2) ➞ 13

football_points(5, 0, 2) ➞ 15

football_points(0, 0, 1) ➞ 0

Notes
Inputs will be numbers greater than or equal to 0.

"""



from edatest import Edatest
Test = Edatest()

def football_points(wins, draws, losses):
    return (wins*3)+(draws*1)+(losses*0)


if __name__ == '__main__':
    Test.assert_equals(football_points(1, 2, 3), 5)
    Test.assert_equals(football_points(5, 5, 5), 20)
    Test.assert_equals(football_points(1, 0, 0), 3)
    Test.assert_equals(football_points(0, 7, 0), 7)
    Test.assert_equals(football_points(0, 0, 15), 0)