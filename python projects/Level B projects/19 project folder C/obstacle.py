
#* Solution starts on line 100.

































































































# #$ Imports.
# from turtle import Turtle
# import random

# #$ Global.
# COLORS = ["lightskyblue", "orange", "purple1", "limegreen", "yellow", "red", "chocolate4"]
# DISTANCE = 5
# INCREMENT = 10

# #$ Class.
# class Car:

#     def __init__(self):
#         self.vehicles = []
#         self.speed = DISTANCE

# #$  How the cars are made and when.        
#     def manufacture(self):
#         chance = random.randint(1, 6)
#         if chance == 1:
#             driver = Turtle("square")
#             driver.shapesize(stretch_wid=1, stretch_len=2)
#             driver.penup()
#             driver.color(random.choice(COLORS))
#             start_y = random.randint(-280, 320)
#             driver.goto(-300, start_y)
#             self.vehicles.append(driver)

# #$  How far the cars are moving.
#     def driving(self):
#         for car in self.vehicles:
#             car.fd(self.speed)

# #$  Increases speed of vehicles.
#     def new_level(self):
#         self.speed += INCREMENT