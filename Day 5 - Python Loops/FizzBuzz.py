
for i in range(1, 101):
    if i %  3 == 0 and i % 5 == 0:
        #Divisible by both 3 & 5
        print("FizzBuzz")
    elif i %  3 == 0:
        #Divisible by 3
        print("Fizz")
    elif i % 5 == 0:
        #Divisible by 5
        print("Buzz")
    else :
        print(i)
        