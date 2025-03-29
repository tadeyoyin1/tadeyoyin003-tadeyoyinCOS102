import random

name_1 = input("Enter your name :")
age_1 = input("Enter your age :")

name_2 = input("Enter your name:")
age_2 = input("Enter your age:")

people = [[name_1 , age_1],[name_2 , age_2]]
random.shuffle(people)


random.shuffle(people)

print("\nShuffled Results:")
for i, (name, age) in enumerate(people, 1):
    print(f"Person {i}: Name = {name}, Age = {age}")