"""
Maximum Difference


Given a list of integers, return the difference between the largest and smallest integers in the list.

Examples
difference([10, 15, 20, 2, 10, 6]) ➞ 18
# 20 - 2 = 18

difference([-3, 4, -9, -1, -2, 15]) ➞ 24
# 15 - (-9) = 24

difference([4, 17, 12, 2, 10, 2]) ➞ 15
"""



from edatest import Edatest
Test = Edatest()

def difference(nums):
    return max(nums)-min(nums)

if __name__ == '__main__':
    Test.assert_equals(difference([-9, -8, 6, -9, 15, 6]), 24)
    Test.assert_equals(difference([-5, 6, 18, 4, 16, -2]), 23)
    Test.assert_equals(difference([-2, 20, -9, -9, -2, -7]), 29)
    Test.assert_equals(difference([4, -2, 11, -9, 15, 2]), 24)
    Test.assert_equals(difference([15, 10, 3, -6, 6, 19]), 25)
    Test.assert_equals(difference([1, 7, 18, -1, -2, 9]), 20)
    Test.assert_equals(difference([5, 1, -9, 7, -8, -10]), 17)
    Test.assert_equals(difference([-4, 17, -4, 20, -7, 0]), 27)
    Test.assert_equals(difference([-2, 11, 11, -3, -3, -3]), 14)
    Test.assert_equals(difference([1, 15, 14, 20, 10, 6]), 19)
    Test.assert_equals(difference([4, 17, 12, 2, 10, 2]), 15)
    Test.assert_equals(difference([-3, 3, 20, 10, 0, 17]), 23)
    Test.assert_equals(difference([-3, 6, 20, 9, 6, 7]), 23)
    Test.assert_equals(difference([16, 15, 1, 18, -7, -3]), 25)
    Test.assert_equals(difference([-7, 4, -4, -3, -8, -9]), 13)
    Test.assert_equals(difference([15, 8, 17, 18, 10, 10]), 10)
    Test.assert_equals(difference([-3, 20, 16, 8, 18, -10]), 30)
    Test.assert_equals(difference([6, 18, 9, 1, 3, 1]), 17)
    Test.assert_equals(difference([20, 18, -2, -10, -10, 17]), 30)
    Test.assert_equals(difference([18, 20, -7, -4, -2, -8]), 28)