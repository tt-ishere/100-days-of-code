weight0 = input("Enter your weight in kg\n")
height0 = input("Enter your height in m\n")

weight1 = float(weight0)
height1 = float(height0)

BMI = str(int(weight1 / (height1 ** 2)))

print("Your BMI is " + BMI)