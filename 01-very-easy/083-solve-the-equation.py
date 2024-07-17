"""
Solve the Equation
Create a function that takes an equation (e.g. "1+1"), and returns the answer.

Examples
equation("1+1") ➞ 2

equation("7*4-2") ➞ 26

equation("1+1+1+1+1") ➞ 5
Notes
Supported operators are +, -, and *.
"""



from edatest import Edatest
Test = Edatest()

def equation(s):
    return eval(s)

if __name__ == '__main__':
    Test.assert_equals(equation("1+1"), 2)
    Test.assert_equals(equation("7*4-2"), 26)
    Test.assert_equals(equation("1+1+1+1+1"), 5)