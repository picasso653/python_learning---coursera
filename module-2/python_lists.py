list1 = [1,2,3,4,5,6,7,8,9,10,11]
print(list1, sep= "")
list1.insert(0, 0)
print(list1, sep= "")
list1.append(12)
print(list1, sep= "")
list1.extend([13, 14, 15])

list2 = ['A', 'B', 'C', 'D', 'E', 'F']

List3 = ["Hello", 1, True, 40.22]
del list2(5)

list4 = [1, [2,3,4], 5]
list4.pop(2)

print(*list1)
print(list2, sep= "")
print(*list4)
