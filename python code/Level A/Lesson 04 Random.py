
#! Randomization and Python lists
#@ Link for Pyhton randomizing functions    https://docs.python.org/3/library/random.html 

#! 1. Import of random module

# import random

#! 2. random.randint(a, b) - A is the starting integer and b is the max range integer

# import random
# random_integer = random.randint(1, 10)
# print(random_integer)

#! 3. random.random() - randomized floating point

# import random
# random_number_0_to_1 = random.random()
# print(random_number_0_to_1)

#! 4. random.uniform(a, b) - 

# import random
# random_float = random.uniform(1, 10)
# print(random_float)

#! 5. randomizing heads and tails

# import random 

# random_coin = random.randint(0, 1)
# if random_coin == 0:
#     print("heads")
# else:
#     print("tails")

#! 6. Lists always use "[]" | typing order = the order of list |
#? Link for Data Structures  https://docs.python.org/3/tutorial/datastructures.html

# States = ["Alabama", "Alaska", "Arizona", "Arkansas", "California", "Colorado", "Connecticut"]

# States[4] = "Cali"

# States.extend(["Wyoming"])

# States.append("Puerto Rico")

# print(States[0], States[4], States[-2], States[-1])

#! 7. randomizing list

# import random
# Cereal = ["Honey Nut Cheerios", "Fruit Loops", "Raisin Bran", "Life", "Fruity Pebbles", "Cinnamon Toast Crunch", "Frosted Flakes"]

# print(random.choice(Cereal))

#! 8. nested lists

# States = ["Alaska", "Alabama", "Arkansas", "Arizona", "California", "Colorado", "Connecticut", "Delaware", "Florida", "Georgia", "Hawaii", "Iowa", "Idaho", "Illinois", "Indiana", "Kansas", "Kentucky", "Louisiana", "Massachusetts", "Maryland", "Maine", "Michigan", "Minnesota", "Missouri", "Mississippi", "Montana", "North Carolina", "North Dakota", "Nebraska", "New Hampshire", "New Jersey", "New Mexico", "Nevada", "New York", "Ohio", "Oklahoma", "Oregon", "Pennsylvania", "Rhode Island", "South Carolina", "South Dakota", "Tennessee", "Texas", "Utah", "Virginia", "Vermont", "Washington", "Wisconsin", "West Virginia", "Wyoming"]

# print(len(States))

# first_half = ["Alaska", "Alabama", "Arkansas", "Arizona", "California", "Colorado", "Connecticut", "Delaware", "Florida", "Georgia", "Hawaii", "Iowa", "Idaho", "Illinois", "Indiana", "Kansas", "Kentucky", "Louisiana", "Massachusetts", "Maryland", "Maine", "Michigan", "Minnesota", "Missouri", "Mississippi"]
# second_half = ["Montana", "North Carolina", "North Dakota", "Nebraska", "New Hampshire", "New Jersey", "New Mexico", "Nevada", "New York", "Ohio", "Oklahoma", "Oregon", "Pennsylvania", "Rhode Island", "South Carolina", "South Dakota", "Tennessee", "Texas", "Utah", "Virginia", "Vermont", "Washington", "Wisconsin", "West Virginia", "Wyoming"]

# the_split = [first_half, second_half]
# print(the_split)