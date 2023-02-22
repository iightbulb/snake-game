from tkinter import S
from turtle import Turtle
import time

STARTING_POSITIONS = [(0, -20), (0, -40), (0, -60)]
MOVE_DISTANCE = 10
UP = 90
DOWN = 270
LEFT = 180
RIGHT = 0

class Snake():       
    def __init__(self) -> None:
        self.my_snake = []
        self.make_snake()
        self.head = self.my_snake[0]

    def make_snake(self):
        for s in STARTING_POSITIONS:
            self.add_segment(s)        

    def add_segment(self, s):
        new_segment = Turtle(shape="square")
        self.recolour(s)
        new_segment.shapesize(0.5)
        new_segment.penup()
        new_segment.goto(s)
        self.my_snake.append(new_segment)
    
    def reset(self):
        for seg in self.my_snake:
            seg.goto(1000, 1000)
        self.my_snake.clear()
        self.make_snake()
        self.head = self.my_snake[0]

    def recolour(self, s):
        for s in self.my_snake[1::2]:
            s.color("light blue")
        for s in self.my_snake[::2]:
            s.color("royal blue")
        
    def extend(self):
        self.add_segment(self.my_snake[-1].position())            
    
    def faster(self):
        self.speed = time.sleep(0.03)
    
    def fasterr(self):
        self.speed = time.sleep(0.02)

    def move(self):
        for seg in range(len(self.my_snake) - 1, 0, -1):
            new_x = self.my_snake[seg - 1].xcor()
            new_y = self.my_snake[seg - 1].ycor()
            self.my_snake[seg].goto(new_x, new_y)
        self.my_snake[0].forward(MOVE_DISTANCE)
    
    def up(self):
        if self.head.heading() != DOWN:
            self.head.setheading(UP)
    
    def down(self):
        if self.head.heading() != UP:
            self.head.setheading(DOWN)
    
    def left(self):
        if self.head.heading() != RIGHT:
         self.head.setheading(LEFT)
    
    def right(self):
        if self.head.heading() != LEFT:
            self.head.setheading(RIGHT)
