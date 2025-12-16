
#! 1. "Subscripting", can use negative numbers
# print("Hello"[-1])

#! 2. "String", variables in quotes
# print("123" + "456")

#! 3. "Integer" = Whole number
# print(123 + 456)

#! 4. "Large Integers"
# print(123_456_789)

#! 5. "Float" = Floating point number
# print(3.14159)

#! 6. "Boolean"
# print(True)
# print(False)

#! 7. "len" function can't process integers.
# print(len("1234576"))

#! 8. "type" function can tell what kind of data type is in its paraenthesis
# print(type("hello"))
# print(type(123))
# print(type(12.412))

#! 9. "type conversion" is for changing data type, sometimes though you cant convert data types
# print(int("789") + int("123"))

#! 10. type conversion for str / string in option 1
    #? OPTION 1 
# name_of_the_user = input("Enter your name")
# length_of_name = len(name_of_the_user)
# print(type("Number of letters in your name: "))  #? string
# print(type(length_of_name))  #? integer

# print("Number of letters in your name: " + str(length_of_name)) # str = string    

    #? OPTION 2
# print("Number of letters in your name: ", + len(input("Enter your name. ")))

#! 11. Math operations
# print("my age: " + str(12))
# print(123 + 456)
# print(7 - 3)
# print(3 * 2)
# print(5 / 3)
# print(5 // 3) #? removes decimal
# print(2**4) #?exponent

#! 12. PEMDAS (), **, * or /, + or -
    #? Order matters, goes left to right 
# print(3 * 3 + 3 / 3 - 3) #? result of 1
# print(3 * ( 3 + 3) / 3 - 3) #? result of 3

#! 13. Calculate BMI
# height = 1.65
# weight = 84
# bmi = (weight / height ** 2)

# print(bmi)
# print(int(bmi)) #cuts off decimal
# print(round(bmi)) #rounds depending on the 1st decimal
# print(round(bmi, 2)) #indicates the amount of decimals rounded to

#! 14. Assignment Operators
# score = 0
# score += 1  #? can change plus out with math punctuation
#             # ?options: += , -= , /= , *=
# print(score)

#! 15. f-strings, used to insert a variable or an expression into a string
# score = 0 
# height = 1.8
# is_winning = True

# print(f"Your score is = {score}, your height is {height}. You are winning is {is_winning}")


#! if you are curious about python Floating point Arithmetic, go this link: https://docs.python.org/3/tutorial/floatingpoint.html