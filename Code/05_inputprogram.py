# name = input("enter your name:")
# print("Hello", name, ", whats up?")


# Ask for the first person's name and age
name1 = input("Enter the name of the first person: ")
age1 = (input("Enter the age of the first person: ")) # use int before (input if whole number requred as an age. with Int user will get error with float numbers.

# Ask for the second person's name and age
name2 = input("Enter the name of the second person: ")
age2 = (input("Enter the age of the second person: "))

# Compare the ages and determine who is younger
if age1 < age2:
    print(f"{name1} is younger than {name2}.")
elif age1 > age2:
    print(f"{name2} is younger than {name1}.")
else:
    print(f"{name1} and {name2} are of the same age.")
