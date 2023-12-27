from turtle import Turtle
FONT = ('Arial', 20, 'normal')
ALIGNMENT = 'center'
class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.score = 0
        
        self.color("white")
        self.penup() 
        self.goto(0,270)
        self.update_score()
        self.hideturtle()
       
    
    def update_score(self):
        self.write(f"Score: {self.score}", move=False,align=ALIGNMENT ,font=FONT)

       
    def game_over(self):
        self.goto(0,0)
        self.write(f"GAME OVER", move=False,align=ALIGNMENT ,font=FONT)


    def add_point(self):
        self.reset()
        self.score += 1
        self.color("white")
        self.penup() 
        self.goto(0,270)
        self.update_score()

        
