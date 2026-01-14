
#!      Create a Phonetic translator for user input word

# TODO: Create a dictionary from 'phonetic'.csv file.
# TODO: Create a way for users to input words. 
# TODO: Print user word out Phonetically.

#*      Solution starts on line 100.



























































































# import pandas   ## 'Pandas': Makes csv file usable.

# data = pandas.read_csv("python projects/Level B projects/22 project folder/phonetic.csv")   ## 'data': Has csv file accessible in shorter context.

# code = {row.Letter:row.Word for (index, row) in data.iterrows()}    ## 'code': Organizes code into dictionary format.

# user = input("Please type a word: ").upper()    ## 'user': Stores input from user in all capitals

# result = [code[Letter] for Letter in user]  ## 'result': Takes every letter from 'user' and finds the dictionary value and key.

# print(result)   ## 'print': Prints to terminal the value from the dictionary that matches the user input as the key.