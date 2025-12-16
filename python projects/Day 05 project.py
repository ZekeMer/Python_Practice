
#TODO Make a randomizing password generator
#! Solution starts on line 100


import random
letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']


print("Welcome to Python Password Maker!!!")

nr_letters = int(input("How many letters would you like?\n"))
nr_symbols = int(input(f"How many symbols would you like?\n"))
nr_numbers = int(input(f"How many numbers would you like?\n"))



















































































# password = []

# for var in range(1, nr_letters + 1):
#     password.append(random.choice(letters))

# for var in range(1, nr_symbols + 1):
#     password += random.choice(symbols)

# for var in range(1, nr_numbers + 1):
#     password += random.choice(numbers)

# random.shuffle(password)
# print(password)

# generate = ""
# for var in password:
#     generate += var

# print(f"Your password is: {generate}")