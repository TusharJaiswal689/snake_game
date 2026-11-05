from turtle import Turtle, Screen
import random

FOOD_RANGE= 250

class Food(Turtle):
    def __init__(self):
        super().__init__()
        self.screen = Screen()
        self.screen.tracer(0)
        self.shape("circle")
        self.color("red")
        self.penup()
        self.shapesize(stretch_len=0.5, stretch_wid=0.5)
        self.speed("fastest")
        self.hideturtle()
        self.is_eaten = True
        self.screen.update()
        self.screen.tracer(1)

    def position_food(self):
        random_x = random.randint(-FOOD_RANGE, FOOD_RANGE)
        random_y = random.randint(-FOOD_RANGE, FOOD_RANGE)

        self.screen.tracer(0)
        self.goto(random_x, random_y)
        self.goto(random_x, random_y)
        self.is_eaten = False
        self.showturtle()
        self.screen.update()
        self.screen.tracer(1)