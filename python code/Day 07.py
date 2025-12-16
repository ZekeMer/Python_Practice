import random
stages = ['''
  +----+   
  |    |    
  O    |   
 /|\   |   
 / \   |
       |
==========  
''', ''' 
  +----+   
  |    |    
  O    |   
 /|\   |   
 /     |
       |
==========  
''', '''  
  +----+   
  |    |    
  O    |   
 /|\   |   
       |
       |
==========  
''', '''  
  +----+   
  |    |    
  O    |   
 /|    |   
       |
       |
==========  
''', '''  
  +----+   
  |    |    
  O    |   
  |    |   
       |
       |
==========  
''', '''  
  +----+   
  |    |    
  O    |   
       |   
       |
       |
==========  
''', '''
  +----+   
  |    |    
       |   
       |   
       |
       |
==========  
''', '''              
          
''']
word_list = ["aardvark", "baboon", "camel", "college", "learn"]


# #! Step 1 of the day
# # TODO Randomly choose a word from the word_list and assign it to a variable called chosen_word. Then print it.
# import random
# chosen_word = random.choice(word_list)
# print(chosen_word)


# # TODO Ask the user to guess a letter and assign their answer to a variable called guess. Make guess lowercase.
# guess = input("guess a letter: ").lower()
# print(guess)



# # TODO Check if the letter the user guessed (guess) is one of the letters in the chosen_word. 
# # TODO Print "Right" if it is correct and "Wrong" if it is not correct.
# for letter in chosen_word:
#     if letter == guess:
#         print("Right")
#     else:
#         print("Wrong")


# #! Step 2
# chosen_word = random.choice(word_list)
# print(chosen_word)

# # TODO Create a "placeholder" with the same number of blanks as the chosen_word.
# placeholder = ""
# word_length = len(chosen_word)

# for position in range(word_length):
#     placeholder += "_"
# print(placeholder)

# guess = input("Guess a letter: ").lower()

# # TODO Create a "display" that puts the guessed letter in the right blank spot.
# display = ""

# for letter in chosen_word:
#     if letter == guess:
#         display += letter
#     else:
#         display += "_"

# print(display)

# #! Step 3
# chosen_word = random.choice(word_list)
# print(chosen_word)

# placeholder = ""
# word_length = len(chosen_word)

# for position in range(word_length):
#     placeholder += "_"
# print(placeholder)

# # TODO Use a while loop to let the user guess again.
# game = False
# correct_letters = []

# while not game:
#     guess = input("Guess a letter: ").lower()

#     display = ""


# # TODO Change the for loops that you keep the previous correct

#     for letter in chosen_word:
#         if letter == guess:
#             display += letter
#             correct_letters.append(guess)
#         elif letter in correct_letters:
#             display += letter
#         else:
#             display += "_"
#     print(display)

#     if "_" not in display:
#         game = True
#         print("You win!")


# #! Step 4
# # TODO Create a cariable called lives to keep track of the number of lives and set live to equal 6.
# lives = 6

# chosen_word = random.choice(word_list)
# print(chosen_word)

# placeholder = ""
# word_length = len(chosen_word)

# for position in range(word_length):
#     placeholder += "_"
# print(placeholder)

# game = False
# correct_letters = []

# while not game:
#     guess = input("Guess a letter: ").lower()

#     display = ""

#     for letter in chosen_word:
#         if letter == guess:
#             display += letter
#             correct_letters.append(guess)
#         elif letter in correct_letters:
#             display += letter
#         else:
#             display += "_"
#     print(display)
# # TODO If guess is not a letter in the chosen_word, reduce lives by 1
# # TODO If lives goes down to 0 then game should end, and print "Game Over!"
#     if guess not in chosen_word:
#         lives -= 1
#         if lives == 0:
#             game = True
#             print("Game Over!")

#     if "_" not in display:
#         game = True
#         print("You win!")

# # TODO Print the ASCII art from stages that corresponds to current number of lives the user has remaining.

#     print(stages[lives])
    