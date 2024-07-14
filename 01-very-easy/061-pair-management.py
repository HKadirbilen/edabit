"""
Pair Management
Given two arguments, return a list which contains these two arguments.

Examples
make_pair(1, 2) ➞ [1, 2]

make_pair(51, 21) ➞ [51, 21]

make_pair(512124, 215) ➞ [512124, 215]
"""



from edatest import Edatest
Test = Edatest()

def make_pair(num1, num2):
    make_pair = []
    make_pair.append(num1)
    make_pair.append(num2)
    return make_pair
    

if __name__ == '__main__':
    Test.assert_equals(make_pair(1, 2), [1, 2])
    Test.assert_equals(make_pair(21, 82), [21, 82])
    Test.assert_equals(make_pair(4213, 526), [4213, 526])