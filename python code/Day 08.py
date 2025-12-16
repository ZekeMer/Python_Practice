
#! Functions with inputs

#! Review of how functions work

# def my_function():          #* Define what the function is.
    
#     print("Test 1")         #? What the Function does and how it does it when called.
    
#     print("Test 2")         #* Make sure everything you want in the function is indented properly.
    
#     print("Test 3")

# my_function()               #? Calling of the function.

# #! Function with 1 input. 

# def my_function(name):
#     print(f"Hello {name}!")
#     print(f"how is your day going {name}?")
# my_function("Jonath")                       #* Input was added to this part of the function

# #! Code to  find out how many weeks a person has to live if max age is 90

# #* Option 1: User inputed option
# age = int(input("how old are you?"))

# def life_in_weeks():
#     person = 90 - age
#     weeks = person * 52
#     print(f"You have {weeks} left to live.")


# life_in_weeks()

# #* Option 2: Hard input, requires manual change in code for changing age.

# def life_in_weeks(age):
#     years_remaining = 90 - age
#     weeks_remaining = years_remaining * 52
#     print(f"You have {weeks_remaining} weeks left.")

# life_in_weeks(12)

# #! Function with more than one input

# #* Positional arguments
# def greet(name, location):      #* Use the order of the inputs to determine the inputs position for calling function.
#     print(f"where is {name}. How is {location}")

# greet("Dominick", "cambridge")   #* This is a positional argument. Depending on the order of the inputs typed, will give you the function input.

# #* Keyword argument

# def greet(name, location):              #? Arguments are identified
#     print(f"Hi {name}")
#     print(f"How is life in {location}?")

# greet(name="Dom", location="Success of the center")     #? Use of identified targets to have them equal a specific string. 
#                                                         #? Regardless of order of Inputs, the argument will have the correct input attached

#* keyword argument practice 

# def calculate_love_score(name1, name2):
#     relate_T = name1.count("t"), name2.count("t")
#     relate_R = name1.count("r"), name2.count("r")
#     relate_U = name1.count("u"), name2.count("u")
#     relate_E = name1.count("e"), name2.count("e")
#     word_one =  sum(relate_T + relate_R + relate_U + relate_E)
#     print(word_one)
#     relate_L = name1.count("l"), name2.count("l")
#     relate_O = name1.count("o"), name2.count("o")
#     relate_V = name1.count("v"), name2.count("v")
#     relate_E2 = name1.count("e"), name2.count("e")
#     word_two = sum(relate_L + relate_O + relate_V + relate_E2)
#     print(word_two)
#     print(f"Love Score = {word_one}{word_two}")
    
    
# calculate_love_score(name1 = "Minecraft Steve", name2 = "Jonathan Ashton-Piper")