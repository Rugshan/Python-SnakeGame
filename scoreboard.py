from turtle import Turtle

TEXT_ALIGNMENT = "center"
FONT = ("Courier", 18, "bold")
SCOREBOARD_VERTICAL_POSITION = 265


class ScoreBoard(Turtle):

    def __init__(self):
        super().__init__()
        self.score = 0
        self.color("white")
        self.hideturtle()
        self.penup()
        self.goto(0, SCOREBOARD_VERTICAL_POSITION)
        self.update_scoreboard()
        self.is_paused = False

    def update_scoreboard(self):
        self.write(f"Score: {self.score}", align=TEXT_ALIGNMENT, font=FONT)

    def increment_score(self):
        self.score += 1
        self.clear()
        self.update_scoreboard()

    def game_over(self):
        self.goto(0, 0)
        self.write("GAME OVER", align=TEXT_ALIGNMENT, font=FONT)

    def toggle_pause_screen(self):

        if not self.is_paused:
            self.is_paused = True
            self.goto(0, 0)
            self.write("PAUSED", align=TEXT_ALIGNMENT, font=FONT)
        else:
            self.is_paused = False
            self.clear()
            self.goto(0, SCOREBOARD_VERTICAL_POSITION)
            self.update_scoreboard()




