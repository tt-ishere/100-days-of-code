import random

from typing import Any
from unicodedata import name

test_seed = int(input("Create a seed number: "))
random.seed(test_seed)

nameasCSV = input("Enter everybody's names seperated by a comma\n")
names = nameasCSV.split(", ")
print(names)
list_num = len(names)
print(list_num)

# generate random number from the 1st to last index of the names list 
rand_name = random.randint(0, list_num -1)
print(f"{names[rand_name]} is going to sponsor us today")