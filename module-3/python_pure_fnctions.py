my_list = [1,2,3,4]

def add_to_list(lst, item):
    nl = lst.copy
    nl.append(item)
    return nl
new_list = add_to_list(my_list, 5)

# Pure functions are not meant to change the values of data outside the scope of the function.