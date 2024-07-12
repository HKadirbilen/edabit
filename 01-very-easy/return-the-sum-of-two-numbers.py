"""
Return the Sum of Two Numbers

Create a function that takes two numbers as arguments and returns their sum.

Examples
addition(3, 2) ➞ 5

addition(-3, -6) ➞ -9

addition(7, 3) ➞ 10
Notes
Don't forget to return the result.
If you get stuck on a challenge, find help in the Resources tab.
If you're really stuck, unlock solutions in the Solutions tab.

"""


from edatest import Edatest
Test = Edatest()

def addition(a, b):
    return a + b


toplam = addition(4,7)
print(toplam)


if __name__ == '__main__':
    Test.assert_equals(addition(2,3), 5)
    Test.assert_equals(addition(-3,-6), -9)
    Test.assert_equals(addition(7,3), 10)