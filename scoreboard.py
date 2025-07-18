from turtle import Turtle
class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.high_score = 0
        self.score = 0
        self.color("white")
        self.penup()
        self.hideturtle()
        self.goto(0, 260)
        self.update_score()
    def update_score(self):
        self.clear()
        self.write(f"score: {self.score} High Score: {self.high_score}", align="center", font=("Arial", 24, "bold"))

    def reset(self):
        if self.score > self.high_score:
            self.high_score = self.score
        self.score = 0
        self.update_score()


    def increase_score(self):
        self.score += 1
        self.update_score()



