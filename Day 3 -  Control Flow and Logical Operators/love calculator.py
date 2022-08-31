print("Welcome to the love calculator")

name1 = input("What is your name?\n")
name2 = input("What is their name?\n")

combine_name = name1 + name2
lowcase_name = combine_name.lower()


# check the number of times the letter of TRUE appear in bothe name
t = lowcase_name.count("t")
r = lowcase_name.count("r")
u = lowcase_name.count("u")
e = lowcase_name.count("e")
true = t + r + u + e

l = lowcase_name.count("l")
o = lowcase_name.count("o")
v = lowcase_name.count("v")
e = lowcase_name.count("e")
love = l + o + v + e    
    
love_score = int(f"{true}{love}")
    
if (love_score < 10) or (love_score > 90):
    print(f"Your score is {love_score}, you go together like coke and mentos.")
elif love_score >= 40 and love_score <= 50:
    print(f"Your score is {love_score}, you are alright together.")
else:
    print(f"Your score is {love_score}.")
