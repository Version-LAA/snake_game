from turtle import Turtle
STARTING_POSITIONS = [(0, 0), (-20, 0), (-40, 0)]
MOVE_DISTANCE = 20
UP = 90
DOWN = 270
LEFT =180
RIGHT = 0
class Snake():
    def __init__(self):
        self.all_snakes = []
        self.create_snake()
        self.head = self.all_snakes[0]
        # self.speed("slow")
        

    def create_snake(self):

        for position in STARTING_POSITIONS:
            self.add_snake(position)
        

    def add_snake(self,position):
        new_snake=Turtle(shape="square")
        new_snake.color("white")
        new_snake.penup()
        new_snake.goto(position)
        self.all_snakes.append(new_snake)
    
    def extend(self):
        self.add_snake(self.all_snakes[-1].position())

    def move(self):
        for seg_num in range(len(self.all_snakes)-1,0,-1):
            new_x = self.all_snakes[seg_num-1].xcor()
            new_y = self.all_snakes[seg_num-1].ycor()
            self.all_snakes[seg_num].goto(new_x,new_y)
        self.head.forward(MOVE_DISTANCE)

    def left(self):
        if self.head.heading() != RIGHT :
            self.all_snakes[0].setheading(LEFT)
    
    def up(self):
        if self.head.heading() != DOWN:
            self.all_snakes[0].setheading(UP)
    
    def right(self):
        if self.head.heading() != LEFT:
            self.all_snakes[0].setheading(RIGHT)
    
    def down(self):
         if self.head.heading() != UP:
            self.all_snakes[0].setheading(DOWN)