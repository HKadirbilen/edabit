"""
Find the Bug: Returning the Container
The packaging system is running wild! The candy is lying loose all over in the warehouse, the cereal is missing, and bread is stuffed in a bottle. What is going on here? The candy should be in plastic and the bread should be in a bag.

The packaging machine is running the get_container() function to retrieve the container of a product. But something is not right...

Examples
get_container("Bread") ➞ "bag"

get_container("Beer") ➞ "bottle"

get_container("Candy") ➞ "plastic"

get_container("Cheese") ➞ None
Notes
Think about what the object's packaging should be.
"""



from edatest import Edatest
Test = Edatest()

"""
fix this code:
def get_container(product):
	matches = {
	"Bread" : "bottle",
	"Milk" : "bottle",
	"Beer" : "bottle",
	"Eggs" : "carton",
	"Cerials" : "box",
	"Candy" : None,
	"Cheese" : None
	}
	return matches[product]
"""

def get_container(product):
	matches = {
	"Bread" : "bag",
	"Milk" : "bottle",
	"Beer" : "bottle",
	"Eggs" : "carton",
	"Cerials" : "box",
	"Candy" : "plastic",
	"Cheese" : None
	}
	return matches[product]

if __name__ == '__main__':
    Test.assert_equals(get_container("Bread"), "bag")
    Test.assert_equals(get_container("Milk"), "bottle")
    Test.assert_equals(get_container("Beer"), "bottle")
    Test.assert_equals(get_container("Eggs"), "carton")
    Test.assert_equals(get_container("Candy"), "plastic")
    Test.assert_equals(get_container("Cheese"), None)