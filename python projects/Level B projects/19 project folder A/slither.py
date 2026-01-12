from turtle import Turtle

STARTING_POS = [(0, 0), (-20, 0), (-40, 0)]
MOVE_DISTANCE = (20)
UP = 90
RIGHT = 0
DOWN = 270
LEFT = 180

#* Solution starts on line 100

























































































# class Snake:

#     def __init__(self):
#         self.body = []
#         self.make_snake()
#         self.head = self.body[0]

#     def make_snake(self):
#         for position in STARTING_POS:
#             self.bigger(position)
   
#     def bigger(self, pos):
#             t = Turtle("square")
#             t.color("White")
#             t.penup()
#             t.goto(pos)
#             self.body.append(t)
    
#     def add_segment(self):
#         self.bigger(self.body[-1].position())
    
#     def movement(self):
#         for body_num in range(len(self.body) - 1, 0, -1):       ## The 'len(body)' allows for the addition of more body segments.
#                                                                 ## The first '-1' is which body segment is being used/starting with.
#                                                                 ## The '0' is the body segment that the for loop is stopping at.
#                                                                 ## The second '-1' is which body segment goes through the for loop next. 

#             x = self.body[body_num - 1].xcor()                  #* Tells the current body segment where the next body segment is on x coordinate.
#             y = self.body[body_num - 1].ycor()                  #* Tells the current body segment where the next body segment is on y coordinate.

#             self.body[body_num].goto(x, y)                      #? Tells the current body segment to move to provided x, y coordinates.

#         self.body[0].forward(MOVE_DISTANCE)                     ## The first body segment moves forward.

#     def right(self):
#         if self.head.heading() != LEFT:                         #* Does not allow the user to go over the body
#             self.body[0].setheading(RIGHT)

#     def up(self):
#         if self.head.heading() != DOWN:
#             self.body[0].setheading(UP)

#     def left(self):
#         if self.head.heading() != RIGHT:
#             self.body[0].setheading(LEFT)

#     def down(self):
#         if self.head.heading() != UP:
#             self.body[0].setheading(DOWN)