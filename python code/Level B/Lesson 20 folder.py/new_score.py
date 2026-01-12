from turtle import Turtle

ALIGNMENT = "center"
FONT = ("Courier", 24, "normal")

with open("python code/Level B/Lesson 20 folder.py/highscore.txt") as number:
    contents = number.read()                ## Reads current number in highscore,txt

HIGH = int(contents)                        ## Converts highscore.txt string to an integer.
    
class Scoreboard(Turtle):

    def __init__(self):
        super().__init__()
        self.score = 0
        self.high_score = HIGH             ## Uses integer format of txt file to provide a number
        self.color("white")
        self.penup()
        self.goto(0, 270)
        self.hideturtle()
        self.update_scoreboard()

    def update_scoreboard(self):
        self.clear()                            ## clears old written scores and updates to new
        self.write(f"Score: {self.score} High Score: {self.high_score}", align=ALIGNMENT, font=FONT)

    def reset(self):                            ## gameover function removed to allow for game to be able to reset.
        if self.score > self.high_score:        ## Changes the highscore if user dies with a higher current score
            self.high_score = self.score
            with open("python code/Level B/Lesson 20 folder.py/highscore.txt", mode="w") as increase:
                increase.write(f"{self.high_score}")    ## Writes over current File number to  replace with new current number.
        self.score = 0                          
        self.update_scoreboard()

    def increase_score(self):
        self.score += 1
        self.update_scoreboard()