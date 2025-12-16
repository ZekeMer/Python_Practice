
#! Python Dictionaries and Nesting

#! Dictionaries

# TODO Leave this section uncommented for the rest of dictionary section to use
# dictionary = {                                                                          #* This is where the start of the dictionary begins. 
#     "Bug": "An error in a program that prevents the program from running as expected.", #? This content is what your dictionary term references.
#     "Function": "A piece of code that you can easily call over and over again.",        #@ The content before ":" is your key value
#     "Loop": "The action of doing something over and over again.",                       #@ The content after ":" is your value for the key.
# }                                                                                       #* Ending point for dictionary

# print(dictionary["Function"])       

#* Adding to dictionary

# dictionary["indentation"] = "Spaces at the begining of a code line."      

#? Clearing a dictionary, needs to be below original dictionary

# dictionary = {}
# print(dictionary)

#? Editing a dictionary, needs to be below original dictionary 

# dictionary["Bug"] = "A moth dead in the computer."
# print(dictionary)

#* Loop through dictionary
# for key in dictionary:
#     print(key)
#     print(dictionary[key])


#! Random Practice

# scores = {
#     'Luke': 88,
#     'Han': 60,
#     'Chewbacca': 95,
#     'C3-PO': 71,
# }

# acceptance = {}

# for person in scores:
#     level = scores[person]

#     if level >= 91:
#         acceptance[person] = "Outstanding"
#     elif level >= 81:
#         acceptance[person] = "Exceeds"
#     elif level >= 71:
#         acceptance[person] = "Okay"
#     else:
#         acceptance[person] = "Go away"

# print(acceptance)


#! Nesting

# #@ Nesting is placing another code structure (i.e., Function, Loop, Dictionaries, List, etc.) inside another code structure.
# #? (EX.) Dictionary = {
# #?                      key: Value, 
# #?                      key2: [list],
# #?                      key3: {Dictionary}
# #?                    }

# #! printing a specific value from a dictionary
# travel_log = {
#     "France": ["Paris", "Lille", "Dijon"]
# }
# print(travel_log["France"][1])  #? The number is indicating what number in the list gets selected.

# #* Accessing 2nd nest and a specific value within
# nested = ["A", "B", ["C", "D"]] #? In order to access second list, the number we need is 2.
# print(nested[2][1])             #? The second list is 3rd in the initial list.

# #! Storing a dictionary in a dictionary.
# dictionary_2 = {                #? The key and value pairs in the additional dictionaries require a colon instead of a equal sign between key and values.
#     "Syzygy": {
#         "def": "Either of two points in the orbit of a solar system body where the body is in opposition to or in conjunction with the sun.",
#         "use": "The first known use if syzygy was circa 1847",
#     },    
#     "Quaff": {
#         "def": "A hearty draft of liquid.",
#         "use": "The first known use of quaff was in 1534",
#     },
#     "Biblioklept": {
#         "def": "A person who steals books",
#         "use": "The first known use of biblioklept was in 1880's",
#     },
#     "Filipendulous": {
#         "def": "suspended by or strung upon a thread",
#         "use": "The first known use of filipendulous was in 1864",
#     },
# }

# print(dictionary_2["Biblioklept"]["use"])