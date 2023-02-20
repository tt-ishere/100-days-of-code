def add(*args):
    sum = 0
    for num in args:
        sum += num
    return sum


print(add(4,50,6, 5))