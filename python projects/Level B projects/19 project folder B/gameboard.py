
#* Solution starts on line 100

































































































# from turtle import Turtle

# class Board(Turtle):

#     def __init__(self, position):
#         super().__init__()
#         self.score = 0
#         self.penup()
#         self.hideturtle()
#         self.goto(position)
       
#     def scoreboard(self):
#         self.color("gold")
#         self.write(f"{self.score}", False, font=("Arial", 25, "normal"))

#     def point(self):
#         self.score += 1
#         self.clear()
#         self.scoreboard()

#     def field(self):
#         self.color("red")
#         self.shape("square")
#         self.setheading(270)
#         for _ in range(10):
#             self.fd(30)
#             self.penup()
#             self.fd(30)
#             self.pendown()

#     def r_win(self):
#         self.color("maroon2")
#         self.goto(-330, 0)
#         self.write(f"Right Side Player Wins!", font=("Arial", 50, "normal"))

#     def l_win(self):
#         self.color("maroon2")
#         self.goto(-330, 0)
#         self.write(f"Left Side Player Wins!", font=("Arial", 50, "normal"))