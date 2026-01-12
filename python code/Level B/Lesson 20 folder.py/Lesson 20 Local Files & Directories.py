
#! Reading text files in read only mode 

# #$ Running with new_file.txt in lesson 20 folder.
# file = open("python code/Level B/Lesson 20 folder.py/new_file.txt", mode="r")     ## Allows Python to open a file. "r" is readonly.
# contents = file.read()                                                            ## Returns contents of file as a string.
# print(contents)
# file.close()                                                                      ## Closes file manually to conserve computer resources.

# #$ Open a txt file with an automatic close.
# with open("python code/Level B/Lesson 20 folder.py/new_file.txt") as file:        ## The 'with' statement allows python to open and close the file when needed.
#     contents = file.read()
#     print(contents)                                               

# #! Writing to text file in write mode.

# with open("python code/Level B/Lesson 20 folder.py/new_file.txt", mode="w") as file: ## Allows Python to open a file. "w" is write.
#     file.write("new 1.")                                                             ## Deletes contents of file and replaces with new text.

# #! Writing to text file in append mode.

# with open("python code/Level B/Lesson 20 folder.py/new_file.txt", mode="a") as file: ## Allows Python to open a file. "a" is to append to file.
#     file.write("\nnew text 2.")                                                      ## Appends the string to a new line of text.

# #! Making new text files using a 'with statement.
# #*  Once ran the file will be made and if you want to see again you need to delete the made file or change name of file being created.
# #*  Only works in write mode, and when file doesnt exist.
# with open("python code/Level B/Lesson 20 folder.py/new_created_file.txt", mode="w") as file:
#     file.write("new file made with this text added.")

# #! Readlines Method.
# file = open("python code/Level B/Lesson 20 folder.py/new_file.txt", mode="r") ## Allows Python to open a file. "r" is readonly.
# print(file.readlines())                                                       ## Prints all lines in text file into a list.

# #! Replace Method.                                                            ## Replaces a specified phrase with another specified phrase.
# txt = "This is Replace"
# x = txt.replace("Replace", "changed")                                         ## Replace swapped for changed
# print(x)

# #! Strip Method.                                                              ## Removes spaces at the beginning and at the end of string.
# text = "   Dom   is ProTute  !        "
# print(text, "Not Stripped")
# y = text.strip()
# print(y, "Stripped")

# #! Adding highscore to Snake game.

# from turtle import Screen
# from new_snake import Snake
# from new_ball import Food
# from new_score import Scoreboard
# import time

# screen = Screen()
# screen.setup(width=600, height=600)
# screen.bgcolor("black")
# screen.title("My Snake Game")
# screen.tracer(0)

# snake = Snake()
# food = Food()
# scoreboard = Scoreboard()

# screen.listen()
# screen.onkey(snake.up, "w")
# screen.onkey(snake.down, "s")
# screen.onkey(snake.left, "a")
# screen.onkey(snake.right, "d")

# game_is_on = True
# while game_is_on:
#     screen.update()
#     time.sleep(0.1)
#     snake.move()

#  #$ Detect collision with food.
#     if snake.head.distance(food) < 15:
#         food.refresh()
#         snake.extend()
#         scoreboard.increase_score()

#  #$ Detect collision with wall.
#     if snake.head.xcor() > 280 or snake.head.xcor() < -280 or snake.head.ycor() > 280 or snake.head.ycor() < -280:
#         scoreboard.reset()                          ## Changes how the scoreboard updates, to reseting current score and updating highscore.
#         snake.reset()                               ## For every new iteration played, send old snake somewhere off screen and has new new snake start from beginning.
#  #$ Detect collision with tail.
#     for segment in snake.segments:
#         if segment == snake.head:
#             pass
#         elif snake.head.distance(segment) < 10:
#             scoreboard.reset()                      ## Changes how the scoreboard updates, to reseting current score and updating highscore.
#             snake.reset()                           ## For every new iteration played, send old snake somewhere off screen and has new new snake start from beginning.


# screen.exitonclick()