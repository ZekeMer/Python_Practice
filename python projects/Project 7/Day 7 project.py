
#! Making the game hangman, with added module files. Also, make it more player friendly visually.
#* Simple solution starts at line 100.
#? Website to reference importing files: https://www.askpython.com/python/python-import-statement 































































































# import random 

#                                     #? 2 methods of importing variables from other files
# from wordlist import word_list      #* First method, pulls specific variable

# import ASCII_Art                    #* Second method, if there's multiple variables, all variables in file are pulled 
# lives = 6

# chosen_word = random.choice(word_list)    #? First method does not require additional inputs.

# placeholder = ""
# word_length = len(chosen_word)
# for position in range(word_length):
#     placeholder += "_"
# print("Word to guess: " + placeholder)

# game = False
# correct_letters = []

# while not game:

#     print(f"*********************{lives}/6 Lives Remaining*************************")
#     guess = input("Guess a letter: ").lower()

#     if guess in correct_letters:
#         print("You have already guessed that letter!!")
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



#     if guess not in chosen_word:
#         lives -= 1
#         print(f"You guessed {guess}, that is not in the word. You have now lost a life!")
#         if lives == 0:
#             game = True
#             print("*********************Game Over, You Lose!!!*********************")
#             print(f"The word was \"{chosen_word}\"")

#     if "_" not in display:
#         game = True
#         print("*********************You Win!*********************")

#     print(ASCII_Art.stages[lives])                #? Method 2 of import requires the addition of the "ASCII_ART." to pull the import