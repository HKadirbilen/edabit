"""
Name Greeting!

Create a function that takes a name and returns a greeting in the form of a string.

Examples
hello_name("Gerald") ➞ "Hello Gerald!"

hello_name("Tiffany") ➞ "Hello Tiffany!"

hello_name("Ed") ➞ "Hello Ed!"

Notes
The input is always a name (as string).
Don't forget the exclamation mark!
If you get stuck on a challenge, find help in the Resources tab.
If you're really stuck, unlock solutions in the Solutions tab.
"""



from edatest import Edatest
Test = Edatest()

def hello_name(name):
    return "Hello " + name + "!"


if __name__ == '__main__':
    Test.assert_equals(hello_name("Gerald"), "Hello Gerald!")
    Test.assert_equals(hello_name("Fatima"), "Hello Fatima!")
    Test.assert_equals(hello_name("Ed"), "Hello Ed!")
    Test.assert_equals(hello_name("Tiffany"), "Hello Tiffany!")