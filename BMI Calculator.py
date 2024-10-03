print("* * * * BMI CALCULATOR * * * *")
weight = int(input("Enter your weight in Kilograms(kg) : "))
height = float(input("Enter your height in Meters(m) : "))

bmi = weight / (height ** 2)

if bmi < 18.5:
    print(f"Your BMI is {bmi:.2f}\nCategory: UNDERWEIGHT")
elif bmi >= 18.5 and bmi < 24.9:
    print(f"Your BMI is {bmi:.2f}\nCategory: NORMAL")
elif bmi >= 24.9 and bmi < 29.9:
    print(f"Your BMI is {bmi:.2f}\nCategory : OVERWEIGHT")
else:
    print(f"Your BMI is {bmi:.2f}\nCategory: OBESE")