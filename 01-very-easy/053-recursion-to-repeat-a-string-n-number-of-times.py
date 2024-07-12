"""
Recursion to Repeat a String n Number of Times

Create a recursive function that takes two parameters and repeats the string n number of times. 
The first parameter txt is the string to be repeated and the second parameter is the number of times the string is to be repeated.

Examples
repetition("ab", 3) ➞ "ababab"

repetition("kiwi", 1) ➞ "kiwi"

repetition("cherry", 2) ➞ "cherrycherry"

Notes
The second parameter of the function is positive integer.
""" 





from edatest import Edatest
Test = Edatest()

def repetition(txt, n):
    return txt * n

if __name__ == '__main__':
    Test.assert_equals(repetition("soccer", 2), "soccersoccer")
    Test.assert_equals(repetition("ab", 3), "ababab")
    Test.assert_equals(repetition("bonita", 1), "bonita")
    Test.assert_equals(repetition("ciao", 4), "ciaociaociaociao")
    Test.assert_equals(repetition("amigo", 5), "amigoamigoamigoamigoamigo")
    Test.assert_equals(repetition("torque", 2), "torquetorque")