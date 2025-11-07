
#! Basic print function
# print("Hello world!\nHello world!")  #? the \n adds new line
# print("Hello" + " Dom") #? catanation
# print("Dom," + " " + "hello!")  #? catanation

#! 1. input function, requires user interaction in terminal.

#input("Where is Dom?")  

#! 2. print function with catanation of input function. input will require answer first before Print will send with input answer in string.

#print("Why is Dom at the" + input("Where is Dom?"))


#! 3. comment line of code allows user to type without effecting the code

# print("Dom is back from " + input("where has dom been? ") + "!")


#! 4. "name" has become variable for the input function

# name = input("what is your name? ")
# print(name)

#! 5. trying to run double prints with same variables

# name = "Dom"
# print(name)
# name = "Jonothan"
# print(name)

#! 6. len = length of string
#?    FYI Highlighting the entire line and putting begining "(" will put the closing ")" at the end of highlighted string.

#print(len(input("Type the word 'Dom'. ")))  

#! 7. putting the functions into different lines and printing both functions.

# name = input("Type the Word 'Dominick'. ")
# length = len(name)
# print(name,""," # of letters is ",length)


#! 8. Pyhtonic Swapping, Switching variable results.
#? variable names should make sense.

# name = "Dominick"
# profession = "Tutor"

# name, profession = profession, name
# print(f"After swapping: name = {name}, profession = {profession}")


#! 10. Multiple input functions with user input, processed into one print statement

# print("Dom's World!!!!!")
# planet = input("What is the best planet? ")
# Dino = input("What is the best dinosaur? ")
# species = input("What species are you? ")
# print("Doms planet is", planet + " Where", Dino + " roam freely, while eating", species)