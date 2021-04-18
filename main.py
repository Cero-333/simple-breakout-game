from turtle import *
from paddle import Paddle
from barrier import Barrier
from ball import Ball
import time

screen = Screen()
screen.bgcolor("black")
screen.setup(width=600, height=600)
screen.title("Break-out Game")

paddle = Paddle()
barrier = Barrier()
ball = Ball()

screen.listen()
screen.onkey(fun=paddle.go_right, key="Right")
screen.onkey(fun=paddle.go_left, key="Left")
screen.tracer(0)

run = True
for _ in range(5):
    barrier.create_barrier_wall()
    barrier.come_down()
screen.update()

rep = 0
while run:
    rep += 1
    if rep % 500 == 0:
        barrier.create_barrier_wall()
        barrier.come_down()
        screen.update()

    time.sleep(ball.move_speed)
    ball.move()

    # collision with side walls and going under the screen
    if ball.xcor() > 290 or ball.xcor() < -290:
        ball.bounce_x()
    elif ball.ycor() > 310:
        ball.bounce_y()
    elif ball.ycor() < - 290:
        ball.reset_position()

    # collision with paddle
    if ball.ycor() < -240 and ball.distance(paddle) < 50:
        ball.bounce_y()

    # collision with barriers
    for x in [y for y in barrier.TURTLES if y.isvisible()]:
        if ball.ycor() > x.ycor() - 20 and ball.distance(x) < 40:
            x.ht()
            ball.move_speed *= 0.99
            ball.bounce_y()
    # There is a little problem with the barrier collisions I cannot seem
    # to find the right numbers for the game to be seem realistic.
    if len([y for y in barrier.TURTLES if y.isvisible()]) == 6:
        print("You won!")
        break

    elif [y for y in barrier.TURTLES if y.isvisible()][0].ycor() < -280:
        print("You lost!")
        break

    screen.update()

screen.exitonclick()
