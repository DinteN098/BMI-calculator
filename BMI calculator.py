import math, time, os

print("Body Mass Index calculator")
print()
print("BMI Categories:\nUnderweight = <18.5\nNoraml weight = 18.5-24.9\nOverweight = 25-29.9\nObesity = BMI of 30 or greater")
print()
weight = float(input("enter your weight in pounds:"))*703

height = (float(input("enter your height in feet:"))*12)**2

bmi = weight/height

print(f"BMI {round(bmi,2)}")
print()
if bmi < 18.5:
    print("You are underweight")
elif bmi >= 18.5 and bmi < 24.9:
    print("You are normal weight")
elif bmi >= 25 and bmi < 29.9:
    print("You are overweight")
else:
    print("Obesity")

print("Program will close in 5 seconds...")
time.sleep(5)  # wait for 5 seconds
os.system("exit")  # close the terminal