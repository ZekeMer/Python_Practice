
#!      Make Turtle crossing game!

# TODO: Move the turtle(Player) with keypress.
# TODO: Create and move cars.
# TODO: Detect collision with cars.
# TODO: Detect when player reaches the other side and increase difficulty.
# TODO: Create a level tracker.

#? Have fun with this and try to customize different parts of the code

#* Solution starts on line 100.























































































# #$ Imports
# from turtle import Screen
# from jay_walker import Walker
# from obstacle import Car
# from gameplay import Text
# import time

# #$ Provides the layout for the Turtle Graphics Screen
# screen = Screen()
# screen.bgcolor("black")
# screen.setup(width=600, height=750)
# screen.tracer(0)

# #$ Providing simpler coding for user to use the classes from other files
# player = Walker()
# car = Car()
# text = Text()

# #$ Provides movement for Player.
# screen.listen()
# screen.onkeypress(player.up, "w")
# screen.onkeypress(player.left, "a")
# screen.onkeypress(player.right, "d")

# #$  Game starting.
# game = True
# while game:
#     time.sleep(0.1)
#     screen.update()
#     car.manufacture()
#     car.driving()

# #$  Player gets hit by car.
#     for distracted_driver in car.vehicles:
#         if distracted_driver.distance(player) < 20:
#             game = False
#             text.hit()

# #$  Player makes it to the finish line. 
#     if player.dodged():
#         player.start_position()
#         car.new_level()
#         text.new_level()

# #$ Keeps screen on until player clicks on screen after losing the game.
# screen.exitonclick()