fruits = ["Apple", "Pear", "Orange"]


# TODO: Catch the exception and make sure the code works

def make_pie(index):
    fruit = fruits[index]
    print(fruit + " pie")


try:
    make_pie(5)

except IndexError:
    print("Fruit pie")
 