"""
WordCharWord
Create a function that will put the first argument, a character, between every word in the second argument, a string.

Examples
add("R", "python is fun") ➞ "pythonRisRfun"

add("#", "hello world!") ➞ "hello#world!"

add("#", " ") ➞ "#"
Notes
Make sure there are no spaces between words when returning the function.
"""



from edatest import Edatest
Test = Edatest()

def add(char, txt):
    if txt.strip() == "":
        return char
    else:
        return char.join(txt.split())
    
    

if __name__ == '__main__':
    Test.assert_equals(add("#", "hello world"), "hello#world")
    Test.assert_equals(add("R", "python is fun"), "pythonRisRfun")
    Test.assert_equals(add("*", "use .join() for this challenge"), "use*.join()*for*this*challenge")
    Test.assert_equals(add("#", " "), "#")