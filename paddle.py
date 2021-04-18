from turtle import Turtle


class Paddle(Turtle):
    def __init__(self):
        super().__init__()
        self.ht()
        self.shape("square")
        self.color("pink")
        self.shapesize(stretch_wid=1, stretch_len=5)
        self.penup()
        self.speed("fastest")
        self.setpos(0, -250)
        self.st()

    def go_right(self):
        current_x = self.xcor()
        self.setx(current_x + 20)

    def go_left(self):
        current_x = self.xcor()
        self.setx(current_x - 20)

