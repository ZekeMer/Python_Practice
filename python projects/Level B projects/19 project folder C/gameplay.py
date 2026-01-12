
#* Solution starts on line 100.

































































































# #$ Imports.
# from turtle import Turtle

# #$ Global.
# FONT = ("Ariel", 24, "normal")

# #$ Class.
# class Text(Turtle):

#     def __init__(self):
#         super().__init__()
#         self.level = 1
#         self.hideturtle()
#         self.penup()
#         self.color("blue")
#         self.goto(-300, 340)
#         self.current_level()

# #$  Write the level during the game.
#     def current_level(self):
#         self.clear()
#         self.write(f"Level: {self.level}", align="left", font=FONT)

# #$  Adds written level.
#     def new_level(self):
#         self.level += 1
#         self.current_level()

# #$  Writes the gameover text and the level player was on.
#     def hit(self):
#         self.goto(-40,0)
#         self.current_level()
#         self.goto(0,40)
#         self.write(f"You've Been Hit!", align="center", font=FONT)