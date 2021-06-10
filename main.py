# w - forward, s- backward, a-counter clockwise,  leftwards,d-right or clockwise, c- clear drawing

from turtle import Turtle, Screen

timmy = Turtle()


def move_forward():
    timmy.forward(10)


def move_backward():
    timmy.backward(10)


def move_right():
    timmy.right(10)


def move_left():
    timmy.left(10)


def clear_screen():
    timmy.reset()


screen = Screen()
screen.listen()
screen.onkey(fun=move_forward, key="w")
screen.onkey(fun=move_backward, key="s")
screen.onkey(fun=move_right, key="d")
screen.onkey(fun=move_left, key="a")
screen.onkey(fun=clear_screen, key="c")

screen.exitonclick()