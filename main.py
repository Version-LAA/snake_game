from turtle import Turtle, Screen


# initial screen configs
screen = Screen()
screen.setup(width=600, height=600)
screen.bgcolor("black")
screen.title("Version_LAA - Snake Game")

#initial snake generation
all_snakes = []
current_x = 0
current_y = 0
for _ in range(3):
    new_snake = Turtle(shape="square")
    new_snake.color("white")
    new_snake.goto(current_x,current_y)
    all_snakes.append(new_snake)
    current_x -= 20



screen.exitonclick()