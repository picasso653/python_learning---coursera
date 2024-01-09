billTotal = 104

discount1 = 10

if billTotal > 100:
    print('Total bill is greater than 100')
    billTotal -= discount1
else:
    print("Bill is less than 100")

print("Total bill is {}".format(billTotal))