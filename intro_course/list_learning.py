
'''
sports = []

print(sports)
print(type(sports))
print(len(sports))
print(sports[0])
print(sports[-1])
print(sports[-2])
print(sports[0:3])
# print(type(sports[0]))
# print(type(sports[1]))
# print(type(sports[2]))
# print(type(sports[3]))
for sport in sports:
    print(type(sport))
    print(sport)
'''

import os

file_path = 'sports01.txt'

def read_sports(file_path):
    if os.path.exists(file_path):
        with open(file_path,'r') as file:
            return [line.strip() for line in file.readlines()]
    return []

def write_sports(file_path, sports_list):
    with open(file_path,'w') as file:
        for sport in sports_list:
            file.write(f"{sport}\n")

repeat = "yes"
while repeat == "yes":
    sports = read_sports(file_path)
# get user input
new_sport = input("Enter your favourite sport: ").capitalize().strip()

if new_sport:
    if new_sport in sports:
        print(f"{new_sport} is already in the list")
    else:
        sports.append(new_sport)
        print("Updated sports list", sports)
else:
    print("No new sport added.")

write_sports(file_path, sports)

print("Sports list:")
for i, sport in enumerate(sports):
    print(f"Sport {i+1}: {sport}")

    repeat = input("Do you want to add another sport? (yes or no): ").strip().lower()
    print("Exiting the program.")
        # asking if the user would like to add another sports.
        # print("Exiting the program.")  # Printing the final message
