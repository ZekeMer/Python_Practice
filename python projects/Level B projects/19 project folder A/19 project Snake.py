
#! Building a Snake game.

# TODO: Make the canvas 600px by 600px
# TODO: Create snake body.
#?      Body consists of 3 squares for the start of the game.
# TODO: Move the snake.
#?      Snake needs to constantly move forward. Add a way for user to make 90 degree directional changes.
# TODO: Detect collision with border and tail. 
# TODO: Add randomly generated food to enlarge the snake.
#?      Each piece of food enlarges snake by 1 square.
# TODO: Create a scoreboard.
#?      Keep track of the amount of food eaten by the snake.
# TODO: Utilize the files provided in the folder to build your game.

#*      Solution starts on line 100

from turtle import Screen
import time                             ## Provides various functions with time-related operations.
from slither import Snake
from food import Mouse
from scoreboard import Score













































































# screen = Screen()
# screen.setup(width=600, height=600)     ## The screens size.
# screen.bgcolor("black")                 ## The screens background color.
# screen.title("The Game of Snake")       ## The title of the screen.
# screen.tracer(0)                        ## turns turtle animation On/Off and set delay for updating the drawing.

# snake = Snake()
# nibble = Mouse()
# score = Score()


# screen.listen()
# screen.onkeypress(snake.right, "d")
# screen.onkeypress(snake.down, "s")
# screen.onkeypress(snake.left, "a")
# screen.onkeypress(snake.up, "w")

# game = True
# while game:
#     screen.update()                                     ## Updates image displayed on screen.

#     time.sleep(0.2)                                     #? Adjust the time between updates.
#     snake.movement()

#     if snake.head.distance(nibble) < 15:                ## Provides collision with food 
#         nibble.new_mouse()
#         snake.add_segment()
#         score.point()        

    
#     if snake.head.xcor() > 290 or snake.head.xcor() < -290 or snake.head.ycor() > 290 or snake.head.ycor() < -290:
#         game = False
#         print(f"You lose! Score of {score.score}, get better Dom!")
        
#     for segment in snake.body:
#         if segment == snake.head:
#             pass
#         elif snake.head.distance(segment) < 5:
#             game = False
#             print(f"Why would you try to eat your own body Dom?!?!?! YOU LOSE with {score.score} points.")
   
# screen.exitonclick()