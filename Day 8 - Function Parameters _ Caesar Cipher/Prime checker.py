#This a prime number checker
def prime_checker(number):
    is_Prime = True
    for i in range(2, number - 1):
        if number % i == 0:
            is_Prime = False
    if is_Prime:
        print("It is a prime number")
    else:
        print("It is not a prime number")

n = int(input("Check this number: "))
prime_checker(number = n)

 