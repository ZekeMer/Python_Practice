
#!      Pong!

# TODO: Create the screen.
# TODO: Create 2 moveable paddles. 
# TODO: Create a moveable ball.
# TODO: Detect collision with walls and a bounce.
# TODO: Detect when paddles miss the ball.
# TODO: Keep score.

#* Solution starts on line 100
























































































# from turtle import Screen 
# from ball import Pong
# from paddle import Paddles
# from gameboard import Board
# import time

# screen = Screen()
# screen.bgcolor("black")
# screen.setup(width=800, height=600)
# screen.tracer(0)

# paddleR = Paddles((360, 0))
# paddleL = Paddles((-370, 0))
# pong = Pong()
# scoreR = Board((175, 250))
# scoreL = Board((-180, 250))
# divider = Board((-5, 320))

# screen.listen()
# screen.onkeypress(paddleR.up, "Up")
# screen.onkeypress(paddleR.down, "Down")
# screen.onkeypress(paddleL.up, "w")
# screen.onkeypress(paddleL.down, "s")

# scoreL.scoreboard()
# scoreR.scoreboard()
# divider.field()

# game = True
# while game:
#     time.sleep(0.008)
#     screen.update()
#     pong.travel()

#     if pong.distance(paddleR) < 50 and pong.xcor() > 350 or pong.distance(paddleL) < 50 and pong.xcor() < -360:
#         pong.hit()

#     if pong.ycor() > 290 or pong.ycor() < -280:
#         pong.ricochet()

#     if pong.xcor() > 380:
#         pong.reset_ping()
#         scoreL.point()
        
#     elif pong.xcor() < -390:
#         pong.reset_ping()
#         scoreR.point()

#     if scoreR.score == 5:
#         scoreR.r_win()
#         game = False
    
#     elif scoreL.score == 5:
#         scoreL.l_win()
#         game = False

# screen.exitonclick()