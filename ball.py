from turtle import Turtle


class Ball(Turtle):
    def __init__(self):
        super().__init__()
        self.shape("circle")
        self.color("white")
        self.penup()
        self.goto(0, -200)
        self.speed("slowest")
        self.bounced_x = 10
        self.bounced_y = 10
        self.move_speed = 0.1

    def move(self):
        new_x = self.xcor() + self.bounced_x
        new_y = self.ycor() + self.bounced_y
        self.goto(new_x, new_y)

    def bounce_y(self):
        self.bounced_y *= -1

    def bounce_x(self):
        self.bounced_x *= -1

    def reset_position(self):
        self.goto(0, -200)
        self.bounce_y()
