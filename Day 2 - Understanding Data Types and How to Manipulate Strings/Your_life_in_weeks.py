print("Welcome to your life in weeks app\n")
print("We will use your age to tell you how many  months, weeks and \n")
print("days you have left if you live up to 90 years\n")

age = int(input("How old are you\n"))

x = (90 - age) * 365
y = (90 - age) * 52
z = (90 - age) * 12

print(f"You have {x} days, {y} weeks and {z} months left to live")