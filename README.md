# BMI-Calculator
This Python script is a Body Mass Index (BMI) Calculator that takes user input for their weight (in kilograms) and height (in meters) to calculate their BMI. BMI is a measure that helps in determining whether a person has a healthy body weight for a given height. The code follows these steps:

User Input:

The program prompts the user to enter their weight in kilograms (int input).
It then asks for the user's height in meters (float input).
BMI Calculation:

The BMI is calculated using the formula:
BMI = weight (kg) / height² (m²)
This formula divides the user's weight by the square of their height to give the BMI value.
Conditional Categorization:

After the BMI is calculated, the program checks which category the user's BMI falls into using conditional if-elif statements:
Underweight: BMI less than 18.5
Normal: BMI between 18.5 and 24.9
Overweight: BMI between 24.9 and 29.9
Obese: BMI greater than or equal to 30
Output:

The user's BMI is printed, rounded to two decimal places, along with the corresponding category based on their BMI.
