"""Demo file to provide examples of how Python's turtle graphic library works!"""

__author__ = "Caitlin Lewis"

# importing all functions from the Python turtle library
from turtle import *

# importing utility functions for drawing shapes
from utility_funcs import *

# a link to the API docs can be found here if you want to check out the available methods:
# https://docs.python.org/3/library/turtle.html

# to have your image drawn you will need to either press the green play button in the top or
# run the following command in your terminal:
# python -m demo

# step 1: instantiating a turtle
turtle1: Turtle = Turtle()

# step 2: calling methods on your turtle
# always use the following syntax:
# turtle_object_variable.method_name()
turtle1.forward(5)

# step 3: drawing shapes
# since we don't have a lot of time in the meeting, we have provided some helpful utility functions for drawing
# they can be found in the utility_funcs.py file



# step 4: goto, penup, pendown

# step 5: pen color, fill color, & other color commands

# step 6: speed and visibility


# in order to prevent the window from closing, place the done() function after all of your turtle drawing code
done()
