print("Welcome to the BMI calculator!!!")

# collecting height and weight data
weight = float(input("Enter your weight in kg: "))
height = float(input("Enter your height in m: "))

# calculating the bmi
bmi = weight / height ** 2
round_bmi = round(bmi,2) #rounding bmi value to 2 decimal places

# BMI interpretation
if round_bmi <= 35:
    if round_bmi < 18.5:
        print(f"Your BMI is {round_bmi} and you're underweight.")
    elif round_bmi < 25:
        print(f"Your BMI is {round_bmi} and you have a normal weight.")
    elif round_bmi < 30:
        print(f"Your BMI is {round_bmi} and you're overweight.")
    else:
        print(f"Your BMI is {round_bmi} and you're obese.")       
else:
    print(f"Your BMI is {round_bmi} and you're clinically obese.")
