
#! Function with Outputs

# def my_function():
#     result = 3 * 5
#     return result             #? Return replaces the part of the code that the function called

# #! Format with ".title", makes the output formatted correctly.
# def format(f_name, l_name):
#     print(f_name.title())
#     print(l_name.title())

# format("Dom", "proTute")
    
# ## For a cleaner version of print.
# def format(f_name, l_name):
#     form_f = f_name.title()
#     form_l = l_name.title()
#     print(f"{form_f} {form_l}")

# format("DoM", "PROtute")
    
# #! Using return to output the new output for function.
# def format(f_name, l_name):
#     form_f = f_name.title()
#     form_l = l_name.title()
#     return f"{form_f} {form_l}"         #? Example of return function 

# form_string = format("DoM", "pRoTuTe")
# print(form_string)

# #! Multiple return values 
# def format(f_name, l_name):
#     if f_name == "" or l_name == "":
#         return "You forgot to type something."
#     form_f = f_name.title()
#     form_l = l_name.title()
#     return f"{form_f} {form_l}"

# print(format(input("What is your First name? "), input("What is your last name? ")))

# #! Return practice
# def is_leap_year(year):
#     year = int(year)
#     if year % 4 == 0:
#         if year % 100 == 0:
#             if year % 400 == 0:
#                 return "It's a leap year."
#             else:
#                 return "It's not a leap year."
#         else:
#             return "It is a leap year."
#     else:
#         return "It is not a leap year"

# year_input = input("What year is it? ")
# result = is_leap_year(year_input)
# print(result)