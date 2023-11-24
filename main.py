from turtle import Turtle, Screen

my_turtle = Turtle()
screen = Screen()





def head_up():
    my_turtle.forward(10)


def head_left():
    new_heading = my_turtle.heading() + 10
    my_turtle.setheading(new_heading)


def head_right():
    new_heading = my_turtle.heading() -10
    my_turtle.setheading(new_heading)


def head_down():
    my_turtle.backward(10)


def clear():
    my_turtle.clear()
    my_turtle.penup()
    my_turtle.home()
    my_turtle.pendown()


screen.listen()

screen.onkey(key="w", fun=head_up)
screen.onkey(key="s", fun=head_down)
screen.onkey(key="a", fun=head_left)
screen.onkey(key="d", fun=head_right)
screen.onkey(key="c", fun=clear)
screen.exitonclick()
