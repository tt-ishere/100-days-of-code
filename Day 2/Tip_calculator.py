from pickletools import float8


print("Welcome to Tip calculator")

total_bill = float(input("What was the total bill?\n $"))
percentage = int(input("Between 10%, 12% or 15%, What percentage tip would you like to give?\n %"))
split = int(input("How many people will split the bill? \n"))

# calculations
percentage1 = (100 + percentage)/100 #markup
tip = total_bill * percentage1 / split # calculating bill with tip then spliting it
rounded_tip = round(tip,2)

print(f"Each person will pay ${rounded_tip}")
      