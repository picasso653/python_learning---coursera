set_a = {0,1,2,3,4,5,6,7,8,9}
print(*set_a)

set_a.discard(9)
print(*set_a)
set_b = {6,7,8,9, 10,11,12,13,14,15}
#print(set_a.union(set_b))
print(set_a | set_b)
#print(set_a.intersection(set_b))
print(set_a & set_b)
#print(set_a.difference(set_b))
print(set_a - set_b)
#print(set_a.symmetric_difference(set_b))
print(set_a ^ set_b)
# Sets don't allow one to input the same value twice
# Meaning if you put in a double number in this list, set will only print one back
# Set usese remove and discard to remove members from their list
# So basically it works like a mathematical set, 
# You can find the intersecion, the Union, the difference and the symmetric difference too
# You can't print the elements of the set based on their index
# It'll return an error saying: 'set' object is not subscriptable
# This means the set is not a sequence
