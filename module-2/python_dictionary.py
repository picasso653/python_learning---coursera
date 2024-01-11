my_d = {1 : 'Test', 'Name': 'Jim'}
print(type(my_d))

my_d[2] = 'Test 2'

my_d[1] = 'Not a Test'

print(my_d)

for key, value in my_d.items():
    print(str(key) + ' : ' + value)

#Dictionary doesn't allow duplicate keys to be set
# If there is a duplicate key, the value of the latest key will be used as the new value