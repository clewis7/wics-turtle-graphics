"""Utility functions for helping to more easily design Python turtle graphics with shapes."""

from turtle import *

NINETY_DEGREE_TURN: float = 90
FASTEST_SPEED: float = 0
SETHEADING: float = 0.0
PIXEL_WIDTH: int = 1500
PIXEL_HEIGHT: int = 800


def draw_rectangle(a_turtle: Turtle, x: float, y: float, length: float, width: float) -> None:
    """Draws a rectangle starting at top left corner located at x, y."""
    a_turtle.penup()
    a_turtle.goto(x, y)
    a_turtle.setheading(SETHEADING)
    a_turtle.pendown()
    a_turtle.speed(FASTEST_SPEED)
    i: int = 0
    a_turtle.begin_fill()
    while i < 2:
        a_turtle.forward(width)
        a_turtle.right(NINETY_DEGREE_TURN)
        a_turtle.forward(length)
        a_turtle.right(NINETY_DEGREE_TURN)
        i = i + 1
    a_turtle.end_fill()
    a_turtle.hideturtle()
    return None


def draw_square(b_turtle: Turtle, x: float, y: float, width: float) -> None:
    """Draws square starting at top-left corner located at x, y."""
    b_turtle.penup()
    b_turtle.goto(x, y)
    b_turtle.setheading(SETHEADING)
    b_turtle.pendown()
    b_turtle.speed(FASTEST_SPEED)
    i: int = 0
    b_turtle.begin_fill()
    while i < 4:
        b_turtle.forward(width)
        b_turtle.right(NINETY_DEGREE_TURN)
        i = i + 1
    b_turtle.end_fill()
    b_turtle.hideturtle()
    return None


def draw_right_triangle(c_turtle: Turtle, x: float, y: float, set_turn: float, leg_1: float, turn_1: float,
                        leg_2: float, turn_2: float, hypotenuse: float) -> None:
    """Draws right rectangle starting at bottom left corner located at x, y."""
    c_turtle.penup()
    c_turtle.goto(x, y)
    c_turtle.setheading(SETHEADING)
    c_turtle.pendown()
    c_turtle.speed(FASTEST_SPEED)
    c_turtle.begin_fill()
    c_turtle.left(set_turn)
    c_turtle.forward(leg_1)
    c_turtle.left(turn_1)
    c_turtle.forward(leg_2)
    c_turtle.left(turn_2)
    c_turtle.forward(hypotenuse)
    c_turtle.end_fill()
    c_turtle.hideturtle()
    return None


def draw_circle(d_turtle: Turtle, x: float, y: float, radius: float) -> None:
    """Draws circle centered at x, y with a radius of radius."""
    d_turtle.penup()
    d_turtle.goto(x, y)
    d_turtle.setheading(SETHEADING)
    d_turtle.pendown()
    d_turtle.speed(FASTEST_SPEED)
    d_turtle.begin_fill()
    d_turtle.circle(radius)
    d_turtle.end_fill()
    d_turtle.hideturtle()
    return None


def draw_line(e_turtle: Turtle, x: float, y: float, length: float, direction: float) -> None:
    """Draws line with length of length at angle of direction."""
    e_turtle.penup()
    e_turtle.goto(x, y)
    e_turtle.setheading(SETHEADING)
    e_turtle.pendown()
    e_turtle.speed(FASTEST_SPEED)
    e_turtle.right(direction)
    e_turtle.forward(length)
    e_turtle.hideturtle()
    return None


def draw_equilateral_tri(f_turtle: Turtle, x: float, y: float, set_turn: float, side_1: float, turn_1: float,
                         side_2: float, turn_2: float, side_3: float) -> None:
    """Draws equilateral triangle starting at bottom left corner located at x, y."""
    f_turtle.penup()
    f_turtle.goto(x, y)
    f_turtle.setheading(SETHEADING)
    f_turtle.pendown()
    f_turtle.speed(FASTEST_SPEED)
    f_turtle.begin_fill()
    f_turtle.left(set_turn)
    f_turtle.forward(side_1)
    f_turtle.left(turn_1)
    f_turtle.forward(side_2)
    f_turtle.left(turn_2)
    f_turtle.forward(side_3)
    f_turtle.end_fill()
    f_turtle.hideturtle()
    return None
