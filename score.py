from turtle import Turtle

class Score(Turtle):
    def __init__(self):
        super().__init__()
        self.score = 0
        with open("data.txt") as data:
            self.high_score =int(data.read())
        self.color("white")
        self.penup()
        self.goto(0, 270)
        self.hideturtle()
        self.update_scorebroad()

    def update_scorebroad(self):
        self.clear()
        self.color("white")
        self.write(f"SCORE : {self.score} High Score : {self.high_score}", align='center', font=('Arial', 18, 'normal'))

    def reset(self):
        if self.score > self.high_score:
            self.high_score = self.score
            with open("data.txt", mode="w") as data:
                data.write(f"{self.high_score}")
        self.score = 0
        self.update_scorebroad()

    def increament_score(self):
        self.score += 1
        self.clear()
        self.update_scorebroad()

    # def game_over(self):
    #     self.goto(0, 0)
    #     self.write(f"GAME OVER!", align='center', font=('Arial', 28, 'normal'))
