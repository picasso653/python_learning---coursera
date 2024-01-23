menu = ['expresso', 'mocha', 'latte', "cappucino", "cortado", "americano"]

def find_coffee(coffee):
    if coffee[0] == "c":
        return coffee

map_coffee = map(find_coffee, menu)

# for i in map_coffee:
#     print(i)
"""
Maps allows you to run a function over all items in a list or any iterable. Bt the catch is:
Map prints whatever the item returns in a list.
"""


filter_coffee = filter(find_coffee, menu)
filter_coffee = [filter for filter in filter_coffee]

print(filter_coffee)

# for i in filter_coffee:
#     print(i)
"""
    filter does the same but different. With filter you get a
 list of items that returned True when passed through the function
    """