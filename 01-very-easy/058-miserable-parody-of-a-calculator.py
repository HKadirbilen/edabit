"""
Miserable Parody of a Calculator

Create a function that will handle simple math expressions. The input is an expression in the form of a string.

Examples
calculator("23+4") ➞ 27

calculator("45-15") ➞ 30

calculator("13+2-5*2") ➞ 5

calculator("49/7*2-3") ➞ 11

Notes
There will be no brackets in the input line.
No need to calculate mathematical functions (sin, cos, ln...).
There are no gaps in the expression.
"""



from edatest import Edatest
Test = Edatest()

def calculator(txt):
    return eval(txt)

if __name__ == '__main__':
    Test.assert_equals(calculator("23+4"), 27)
    Test.assert_equals(calculator("45-15"), 30)
    Test.assert_equals(calculator("13+2-5*2"), 5)
    Test.assert_equals(calculator("49/7*2-3"), 11)
    Test.assert_equals(calculator("2+2*2"), 6)
    Test.assert_equals(calculator("5/2"), 2.5)
    Test.assert_equals(calculator("-34/4"), -8.5)
    Test.assert_equals(calculator("0+43-0+56*0"), 43)
    Test.assert_equals(calculator("-14*2-37-0"), -65)
    Test.assert_equals(calculator("0*0"), 0)
    Test.assert_equals(calculator("4+2+3-5*2-8/4-12-0+3-14"), -26)
    Test.assert_equals(calculator("9/2+9/4"), 6.75)
    Test.assert_equals(calculator("56*27*18*12/2*0"), 0)
    Test.assert_equals(calculator("34/4*0*45*7"), 0)
