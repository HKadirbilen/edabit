"""
Evaluate an Equation
Create a function that evaluates an equation.

Examples
eq("1+2") ➞ 3

eq("6/(9-7)") ➞ 3

eq("3+2-4") ➞ 1
Notes
Don't print, return a value.
Return the value, not the equation.
The method used to solve this challenge should not be used in practice. 
However, it's important to be aware of how this functionality works and why it should not be used. Check the Resources for more information.
"""



from edatest import Edatest
Test = Edatest()

def eq(evaluate):
    return eval(evaluate)

if __name__ == '__main__':
    Test.assert_equals(eq("1+2"), 3)
    Test.assert_equals(eq("6/(9-7)"), 3)
    Test.assert_equals(eq("3+2-4"), 1)
    Test.assert_equals(eq("3*4+1"), 13)
    Test.assert_equals(eq("5*8-4*9"), 4)
    Test.assert_equals(eq("3**7"), 2187)
    Test.assert_equals(eq("(6**3)+3"), 219)