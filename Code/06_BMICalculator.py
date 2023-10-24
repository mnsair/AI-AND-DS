# Ask for the person's name
name = input("Enter your name: ")

# Ask for the person's age
age = int(input("Enter your age: "))

# Ask for the person's weight in pounds
weight_pounds = float(input("Enter your weight in pounds: "))

# Ask for the person's height in inches
height_inches = float(input("Enter your height in inches: "))

# Calculate BMI
# 1 pound = 0.453592 kilograms
# 1 inch = 0.0254 meters
weight_kg = weight_pounds * 0.453592
height_m = height_inches * 0.0254

bmi = weight_kg / (height_m ** 2)

# Print the result
print(f"Hello, {name}! Your BMI is {bmi:.2f}.")