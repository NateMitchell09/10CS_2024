# Get the user to input their name
# Get the user tp input their birth year
# Calculate the users age
# Expected output: "Hi NAME, you are 15 years old." as an F-string
# Test the program with your own name and birth year
# Test with my name and birth year 1976, and I am not 48 years old.
import os

repeat = "yes"
while repeat == "yes":
    name = input("Enter your name: ").strip()
    birth_year = int(input("Enter your birth year: ").strip())
    age = 2024 - birth_year

    birthday = input("have you had your birthday already this year? (Yes/No): ").lower().strip()
    if birthday == "no":
        age = age - 1
    # This code subtracts a year if user didn't have their birthday that year to get the users correct age

    print(f" Hi {name}, you are {age} years old. ")
    # Expected output, "Hi NAME, you are 15 years old." as an F-string.
    repeat = input("Would you like to run the program again? (yes/no): ").lower().strip()
    os.system('cls||clear')
# if repeat == "no": thank the user and exit program
print("Thank you for using the age calculator.")
