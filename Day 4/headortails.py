import random

test_seed = int(input("Create a seed number: "))
random.seed(test_seed)

randtoss = random.randint(0,1)

if randtoss == 0 :
    print("Tails")
else:
    print("Heads")
