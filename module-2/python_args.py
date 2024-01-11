def sum_of(*args):
    sum = 0
    for i in args:
        sum += i
    return sum

print(sum_of(3,4,5,6))