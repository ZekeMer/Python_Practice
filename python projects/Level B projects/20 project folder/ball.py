
#* Solution starts on line 100

































































































# from turtle import Turtle
# import random

# varient = [-1, 1]

# class Pong(Turtle):

#     def __init__(self):
#         super().__init__()
#         self.shape("turtle")
#         self.penup()
#         self.color("deepskyblue3")
#         self.y_loc = 1
#         self.x_loc = 1
#         self.velocity = 0.1
        

#     def travel(self):
#         new_x = self.xcor() + self.x_loc
#         new_y = self.ycor() + self.y_loc
#         self.goto(new_x, new_y)

#     def ricochet(self):
#         self.y_loc *= -1

#     def hit(self):
#         self.x_loc *= -1
#         self.velocity *= 0.9

#     def reset_ping(self):
#         self.goto(0,0)
#         self.y_loc *= random.choice(varient)
#         self.x_loc *= random.choice(varient)