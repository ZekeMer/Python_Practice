#day 3 excersices 
#! 1. if / else statements

# print("Welcome to the rollercoaster!")
# height = int(input("What is your height in cm? "))

# if height >= 120:
#     print("You can ride the rollercoaster.")

# else:
#     print("Get taller Dominick!")

#? Comparison Operators:
#*      >       Greater than
#*      <       Less than
#*      >=      Greater than or equal to
#*      <=      Less than or equal to
#*      ==      Equal to
#*      !=      Not equal to

#! 2. Modulo Operator  (%)   AKA remainder of equation will be result

# number_to_check = int(input("What is the number you want to check? "))

# if number_to_check % 2 == 0:
#     print("even")

# else:
#     print("odd")

#! 3. Nested if/else statements

# print("Welcome to the roolercoaster!")
# height = int(input("What is your height in cm? "))

# if height >= 120:
#     print("You can ride the rollercoaster")
#     age = int(input("What is your age? "))
#     if age <= 12:
#         print("Please pay $5.")
#     elif age <= 18:
#         print("Please pay $6.")
#     else: 
#         print("You can ride for free.")
# else:
#     print("Sorry you need to get on Dominick's shoulders to ride!")

#! 4. Multiple If conditions

# print("Welcome to the roolercoaster!")
# height = int(input("What is your height in cm? "))

# if height >= 120:
#     print("You can ride the rollercoaster")
#     age = int(input("What is your age? "))
#     if age <= 12:
#         print("Ticket will be $5.")
#         bill = 5
#     elif age <= 18:
#         print("Ticket will be $6.")
#         bill = 5
#     else:
#         bill = 0 
#         print("Ticket will be free.")
    
#     want_photo = input("Do you want to have a photo taken? Type Y for yes and n for No. ")
#     if want_photo == "y":
#         bill += 3
    
#     print(f"your final bill is ${bill}")


# else:
#     print("Sorry you need to get on Dominick's shoulders to ride!")

#! 5. Pizza order practice

# print("Welcome to the Pizza factory")

# size = input("What size pizza would you like? S, M, L, XL: ")

# if size == "S":
#     print("Must be on a diet.")
#     bill = 5
# elif size == "M":
#     print("Always good to have a nice snack.")
#     bill = 7
# elif size == "L":
#     print("Meal time already.") 
#     bill = 9
# elif size == "XL":
#     print("Now that is a good appetite.")
#     bill = 11
# else:
#     print("Please don't block the line for paying customers")
#     exit()  


# pepperoni = input("Would you like pepperoni? Y or N: ")
# if pepperoni == "Y":
#     print("That will be an extra 1 dollar")
#     bill += 1

# cheese = input("Would you like extra cheese? Y or N: ")
# if cheese == "Y":
#     print("That will be an extra 50 cents.")
#     bill += 0.50

# print(f"Your total is ${bill:.2f}") 

#! 6. Logical operations
#?      and, or, not

# print("Welcome to the roolercoaster!")
# height = int(input("What is your height in cm? "))
# bill = 0

# if height >= 120:
#     print("You can ride the rollercoaster")
#     age = int(input("What is your age? "))
#     if age <= 12:
#         print("Ticket will be $5.")
#         bill = 5
#     elif age <= 18:
#         print("Ticket will be $6.")
#         bill = 5
#     elif age >= 45 and age <= 55:       #? can look like (45 >= age <= 55)
#         print("Everyhthing is going to be ok. Have a free ride on us!")
#     else:
#         bill = 0 
#         print("Ticket will be free.")
    
#     want_photo = input("Do you want to have a photo taken? Type Y for yes and n for No. ")
#     if want_photo == "y":
#         bill += 3
    
#     print(f"your final bill is ${bill}")


# else:
#     print("Sorry you need to get on Dominick's shoulders to ride!")
