
#! List Comprehesion

#? list = [A]                               ## Starting list.
                                            ## 'A': Item in the list.
#? new_list = [B for item in list]          ## Created new list.
                                            ## 'B': New item that is added to 'new_list'.
                #* 'B': Operation that happens for new item creation.
                #* 'item': An item from the starting list.
                #* 'list': Starting list you are pulling 'item' from.

#$ Example of Appending to new List: 
numbers = [1, 2, 3, 4, 5]                   ## Starting list with starting items.
new_numbers = []                            ## New list that will hold new items.
for n in numbers:                           ## 'n': the starting list items. 
                #* 'n': Item from the starting list.
                #* 'numbers': The list you are pulling an item from.
    add = n + 1                             ## 'n + 1': n grabs first item from starting list adds 1, then repeats for all items in list. 
                #* 'n + 1': Operation that happens for a new variable to be created.
    new_numbers.append(add)                 ## Adds the each created variable 'add' to new list as items.
                #* 'append': Adds the newly created variable to the new list. 
print("\nAppending to new list:", new_numbers)                          ## Result of new list after 'for loop' finishes running.

#$ Example of List Comprehension (List):

num = [2, 3, 4, 5, 6]                       ## Starting list with starting items.
new_num = [n -  1 for n in num]             ## New list that will hold new items.
                #* 'n - 1': Operation that happens to create new item.
                #* 'n': An item from the starting list.
                #* 'num': Starting list you are pulling 'n' from.
print("\nList Comprehension (List):", new_num)

#$ Example 2 of List comprehension (String):

name = "Dom"                                ## Starting Variable with String.
letters_name = [letter for letter in name]  ## New list that will hold new items.
                #* 1st 'letter': Operation for new item creation.
                #* 2nd 'letter': Identifies each letter in String as an item.
                #* 'name': Variable that you are pulling the String from.
print("\nList Comprehension (String):", letters_name)

#$ Example 3 of List Comprehension (Range):

r_list = [r_num * 2 for r_num in range(1,5)]## New list being created.
                #* 'r_num * 2': Operation for new item creation.
                #* 'r_num': A number being pulled from the range.
                #* 'range(1,5): The numbers in the range are 1, 2, 3, 4.
print("\nList Comprehesion (range):", r_list)

#! Conditional List Comprehension

#? list = [1, 20, 300, 4000, 50000, 600000] ## Starting list of numbers as the items.

#? new_list = [number for number in list if number < 4001] ## New list being created.
                #* 1st 'number': Operation that happens for new item creation.
                #* 2nd 'number': Item from the starting list.
                #* 'list: Starting list you are pulling 'item' from.
                #* 3rd 'number < 4001: "Testing" the new item before it gets added to 'new_list' 

#$ Example of conditional List Comprehension:

colors = ["Red", "Orange", "Yellow", "Green", "Blue", "Purple"]
no_test_list = [name for name in colors]
with_test_list = [name for name in colors if len(name) > 5]
print("\ntest NOT included:", no_test_list)
print("\nTEST INCLUDED:", with_test_list)

#$ Example of conditional List Comprehension with Uppercased letters:

dom = ["Protute", "Tutor", "Student", "Winner", "Dungeon Master", "Professional", "Nerd", "Hardworker", "Tired"]
test_no = [n for n in dom]
one_test = [n for n in dom if len(n) > 5]
two_test = [n.upper() for n in dom if len(n) > 5 and len(n) < 8]
print("\nNo Test:", test_no)
print("\nOne Test Included:", one_test)
print("\nTwo Tests Included and all Letters Uppercase:", two_test)

#! Dictionary Comprehension

#? new_dictionary = {new_key:new_value for item in list}
                #* 'new_key': The new Key in the new Dictionary.
                #* 'new_value': The new Value in the new Dictionary.
                #* 'item': Item from List that is being added as Key or Value in new Dictionary.
                #* 'list': The List that is providing Items.

#? 2nd_new_dictionary = {new_key:new_value for (key,value) in dict.items()}
                #* 'new_key': The new Key in the new Dictionary.
                #* 'new_value': The new Value in the new Dictionary.
                #* '(key,value)': Key and Value from starting Dictionary.
                #* 'dict.items()': The starting Dictionary providing the Key and Values.

#$ Example of Dictionary Comprehension with a List:

import random

items = ["Ball", "Racket", "Bowl", "Spork", "Table", "Stairs", "Ceiling", "Keyboard"]
item_with_number = {item:random.randint(1,58) for item in items}
print("\nDictionary Comprehension (List):", item_with_number)

#$ Example of Dictionary Comprehension with another Dictionary

starting_dictionary = {
    "Ball": 14,
    "Racket": 52,
    "Bowl": 28,
    "Spork": 21,
    "Table": 50,
    "Stairs": 51,
    "Ceiling": 49,
    "Keyboard": 43
}

update_dict = {object:num + 1 for (object, num) in starting_dictionary.items()}
print("\nDictionary Comprehension (Dictionary):", update_dict)

#! Conditional Dictionary Comprehension

#? con_new_dict = {new_key:new_value for (key,value) in dict.items() if test}
                #* 'new_key': The new Key in the new Dictionary.
                #* 'new_value': The new Value in the new Dictionary.
                #* '(key,value)': Key and Value from starting Dictionary.
                #* 'dict.items()': The starting Dictionary providing the Key and Values.
                #* 'test': Provides condition for new Key and new Values to be added to new Dictionary.

#$ Example of Conditional Dictionary Comprehension with another dictionary

starting_dictionary2 = {
    "Ball": 14,
    "Racket": 52,
    "Bowl": 28,
    "Spork": 21,
    "Table": 50,
    "Stairs": 51,
    "Ceiling": 49,
    "Keyboard": 43
}

update_dict2 = {object:num for (object, num) in starting_dictionary2.items() if num > 45}
print("\nConditional Dictionay Comprehension:", update_dict2, "\n")

#! Iterate with Pandas DataFrame

import pandas

weather = pandas.read_csv("python code/Level B/Lesson 22 folder/weather.csv")

for (index, row) in weather.iterrows():     ## Filter horizontally.
    print("\nRow (index):", index)
    print("\nRow (row):", row)
for (index, row) in weather.items():        ## Filter vertically.
    print("\nColumn (index):", index)
    print("\nColumn (row):", row)