from turtle import *
import random

X_COORDINATES = [-250, -150, -50, 50, 150, 250]
COLORS = ["pink", "white", "green", "blue", "red", "orange", "purple", "yellow", "brown", "grey"]


class Barrier:
    def __init__(self):
        self.TURTLES = []
        self.STAMP_IDS = []
        self.create_barrier_wall()

    def create_barrier_wall(self):
        colour = random.choice(COLORS)
        for i in X_COORDINATES:
            a = Turtle()
            a.ht()
            a.penup()
            a.shape("square")
            a.color(colour)
            a.shapesize(stretch_wid=1, stretch_len=4)
            a.speed("fastest")
            a.setpos(i, 280)
            a.st()
            self.TURTLES.append(a)
            self.STAMP_IDS.append(a.stamp())

    def come_down(self):
        for turtle in self.TURTLES:
            turtle.speed("slowest")
            current_y = turtle.ycor()
            turtle.sety(current_y - 30)
