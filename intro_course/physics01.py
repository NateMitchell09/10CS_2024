# Variables
# Variables are used to store data in a program.
# In python, variables are created by assigning a value to a meaningful name.
# The value of a variable can be changed or updated throughout the program.
# Variables contain one type of data at a time, but the data type can change.
# Data types in python include integers, floats, strings, and booleans.
'''
name = "Fred" # this variable contains a string 'str' which is (text)
age = 15 # this variable contains an integer 'int' which is a whole number
salary = 100 # this variable contains a float 'float' which is a decimal number
is_student = True #
'''
# Change the above variables to take input from the user
name = "Fred"  # string (str).
age = 15  # integer (int).
salary = 1000.50  # float.
is_student = True  # bool.

name = input("Enter your name: ")
age = int(input("Enter your age: "))
salary = float(input("Enter your salary: "))
is_student = bool(input("Are you a student? (True/False): "))

print(type(name))
print(type(age))
print(type(salary))
print(type(is_student))
# line above all are not printed and going into the F-string which is being printed
print("Name: ", name)
if is_student == True:
    student= "Yes"

else:
    student= "No"

# the following is an F-string
print(f"{name} is {age} years old and earns $ {salary} per month. Is he a student? {is_student}")
print(f"{name} is {age} 'years old' and earns $ {salary} per month. Is he a student? {student}")
# printing the name, age, salary and occupation of "fred" into a full sentence.
