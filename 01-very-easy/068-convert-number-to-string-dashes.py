"""
Convert Number to String of Dashes
Create a function that takes a number (from 1 - 60) and returns a corresponding string of hyphens.

Examples
num_to_dashes(1) ➞ "-"

num_to_dashes(5) ➞ "-----"

num_to_dashes(3) ➞ "---"
Notes
You will be provided integers ranging from 1 to 60.
Don't forget to return your result as a string.
If you get stuck on a challenge, find help in the Resources tab.
If you're really stuck, unlock solutions in the Solutions tab.
"""



from edatest import Edatest
Test = Edatest()

def num_to_dashes(num):
    return num * "-"

if __name__ == '__main__':
    Test.assert_equals(num_to_dashes(1),"-")
    Test.assert_equals(num_to_dashes(2),"--")
    Test.assert_equals(num_to_dashes(3),"---")
    Test.assert_equals(num_to_dashes(4),"----")
    Test.assert_equals(num_to_dashes(5),"-----")
    Test.assert_equals(num_to_dashes(6),"------")
    Test.assert_equals(num_to_dashes(7),"-------")
    Test.assert_equals(num_to_dashes(8),"--------")
    Test.assert_equals(num_to_dashes(9),"---------")
    Test.assert_equals(num_to_dashes(10),"----------")
    Test.assert_equals(num_to_dashes(11),"-----------")
    Test.assert_equals(num_to_dashes(12),"------------")
    Test.assert_equals(num_to_dashes(13),"-------------")
    Test.assert_equals(num_to_dashes(14),"--------------")
    Test.assert_equals(num_to_dashes(15),"---------------")
    Test.assert_equals(num_to_dashes(16),"----------------")
    Test.assert_equals(num_to_dashes(17),"-----------------")
    Test.assert_equals(num_to_dashes(18),"------------------")
    Test.assert_equals(num_to_dashes(19),"-------------------")
    Test.assert_equals(num_to_dashes(20),"--------------------")
    Test.assert_equals(num_to_dashes(21),"---------------------")
    Test.assert_equals(num_to_dashes(22),"----------------------")
    Test.assert_equals(num_to_dashes(23),"-----------------------")
    Test.assert_equals(num_to_dashes(24),"------------------------")
    Test.assert_equals(num_to_dashes(25),"-------------------------")
    Test.assert_equals(num_to_dashes(26),"--------------------------")
    Test.assert_equals(num_to_dashes(27),"---------------------------")
    Test.assert_equals(num_to_dashes(28),"----------------------------")
    Test.assert_equals(num_to_dashes(29),"-----------------------------")
    Test.assert_equals(num_to_dashes(30),"------------------------------")
    Test.assert_equals(num_to_dashes(31),"-------------------------------")
    Test.assert_equals(num_to_dashes(32),"--------------------------------")
    Test.assert_equals(num_to_dashes(33),"---------------------------------")
    Test.assert_equals(num_to_dashes(34),"----------------------------------")
    Test.assert_equals(num_to_dashes(35),"-----------------------------------")
    Test.assert_equals(num_to_dashes(36),"------------------------------------")
    Test.assert_equals(num_to_dashes(37),"-------------------------------------")
    Test.assert_equals(num_to_dashes(38),"--------------------------------------")
    Test.assert_equals(num_to_dashes(39),"---------------------------------------")
    Test.assert_equals(num_to_dashes(40),"----------------------------------------")
    Test.assert_equals(num_to_dashes(41),"-----------------------------------------")
    Test.assert_equals(num_to_dashes(42),"------------------------------------------")
    Test.assert_equals(num_to_dashes(43),"-------------------------------------------")
    Test.assert_equals(num_to_dashes(44),"--------------------------------------------")
    Test.assert_equals(num_to_dashes(45),"---------------------------------------------")
    Test.assert_equals(num_to_dashes(46),"----------------------------------------------")
    Test.assert_equals(num_to_dashes(47),"-----------------------------------------------")
    Test.assert_equals(num_to_dashes(48),"------------------------------------------------")
    Test.assert_equals(num_to_dashes(49),"-------------------------------------------------")
    Test.assert_equals(num_to_dashes(50),"--------------------------------------------------")
    Test.assert_equals(num_to_dashes(51),"---------------------------------------------------")
    Test.assert_equals(num_to_dashes(52),"----------------------------------------------------")
    Test.assert_equals(num_to_dashes(53),"-----------------------------------------------------")
    Test.assert_equals(num_to_dashes(54),"------------------------------------------------------")
    Test.assert_equals(num_to_dashes(55),"-------------------------------------------------------")
    Test.assert_equals(num_to_dashes(56),"--------------------------------------------------------")
    Test.assert_equals(num_to_dashes(57),"---------------------------------------------------------")
    Test.assert_equals(num_to_dashes(58),"----------------------------------------------------------")
    Test.assert_equals(num_to_dashes(59),"-----------------------------------------------------------")
    Test.assert_equals(num_to_dashes(60),"------------------------------------------------------------")