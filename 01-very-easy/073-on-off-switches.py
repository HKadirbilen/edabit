"""
On/Off Switches
Create a function that returns how many possible arrangements can come from a certain number of switches (on / off). In other words, for a given number of switches, how many different patterns of on and off can we have?

Examples
pos_com(1) ➞ 2

pos_com(3) ➞ 8

pos_com(10) ➞ 1024
Notes
All numbers will be whole and positive.
"""



from edatest import Edatest
Test = Edatest()

def pos_com(num):
    return 2 ** num

if __name__ == '__main__':
    Test.assert_equals(pos_com(5), 32)
    Test.assert_equals(pos_com(4), 16)
    Test.assert_equals(pos_com(3), 8)
    Test.assert_equals(pos_com(2), 4)
    Test.assert_equals(pos_com(1), 2)
    Test.assert_equals(pos_com(6), 64)
    Test.assert_equals(pos_com(7), 128)
    Test.assert_equals(pos_com(8), 256)
    Test.assert_equals(pos_com(9), 512)
    Test.assert_equals(pos_com(10), 1024)
    Test.assert_equals(pos_com(25), 33554432)