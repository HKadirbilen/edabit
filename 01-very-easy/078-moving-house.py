"""
Moving House
I'd like to calculate how long on average I've lived in the same house.

Given a person's age and the number of times they've moved house as moves, return the average number of years that they've spent living in the same house.

Examples
years_in_one_house(30, 1) ➞ 15

years_in_one_house(15, 2) ➞ 5

years_in_one_house(80, 0) ➞ 80
Notes
You can assume that the tests include people who've always lived in a house.
Round to the nearest year.
"""



from edatest import Edatest
Test = Edatest()

def years_in_one_house(age, moves):
    return round(age / (moves + 1))

if __name__ == '__main__':
    Test.assert_equals(years_in_one_house(30, 1), 15)
    Test.assert_equals(years_in_one_house(15, 2), 5)
    Test.assert_equals(years_in_one_house(80, 0), 80)
    Test.assert_equals(years_in_one_house(23, 2), 8)
    Test.assert_equals(years_in_one_house(31, 2), 10)
    Test.assert_equals(years_in_one_house(1, 0), 1)