
#* Solution starts on line 100.

































































































# #$ Imports
# from turtle import Turtle
# import random

# #$ Global
# POSITION = 0, -350
# COLOR = ["deeppink", "cyan", "greenyellow", "magenta", "yellow", "azure"]

# #$ Class
# class Walker(Turtle):

#     def __init__(self):
#         super().__init__()
#         self.shape("turtle")    
#         self.penup()
#         self.start_position()
#         self.setheading(90)

# #$ Allows player to move up the board.
#     def up(self):
#         self.fd(10)

# #$  Allows player to move left and by how far.
#     def left(self):
#         if self.xcor() > -270:
#             slideL = self.xcor() - 20
#             self.goto(slideL, self.ycor())

# #$  Allows player to move right and by how far.
#     def right(self):
#         if self.xcor() < 270:
#             slideR = self.xcor() + 20
#             self.goto(slideR, self.ycor())

# #$  Where the turtle starts at.
#     def start_position(self):
#         self.goto(POSITION)
#         self.color(random.choice(COLOR))

# #$  Letting the game know the Player made it across the road.
#     def dodged(self):
#         if self.ycor() > 360:
#             return True
#         else:
#             return False