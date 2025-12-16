
#! 1. For Loop

# fruits = ["Apple", "Peach", "Pear"]
# print(fruits)
# for fruit in fruits:
#     print(fruit)
#     print(fruit + " pie")

# print(fruits)

#! 2. Function: Sum, Max

# num = [ 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 112, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21]

# totals = sum(num)

# print(max(num))

# sum = 0
# for number in num:
#     sum += number

# print(sum)

#! Highest score

# student_score = [ 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 112, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21]

# max_score = 0
# for score in student_score:
#     if score > max_score:
#         max_score = score

# print(max_score)

#! For Loops with Range
#? for number in range(a, b):       
#?     print(number) 
#* the range function defines the numbers between a and b.

#! Part A
# for number in range(1, 11):
#     print(number)           #* counts 1 to 10 

#! Part B
# for number in range(1, 10, 3):
#     print(number)           #* the 3 in range has the counting happen by 3

#! Part C
# total = 0
# for number in range (1, 101):
#     total += number
# print(total)                #* += adds all numbers together in the range from 1 to 100

#! Part D
#? Print each number from 1 to 100
#? If number is divisible by 3 have the word tree display instead of number
#? If number is divisible by 5 have the word fife display instead of number
#? if number is divisble by both 3 and 5 have treefife displayed instead of number

# total = 0
# for number in range(1, 101):
#     if number % 3 == 0 and number % 5 == 0:
#         print("treefife")
#     elif number % 3 == 0:
#         print("tree")
#     elif number % 5 == 0:
#         print("fife")
#     else:
#         print(number)