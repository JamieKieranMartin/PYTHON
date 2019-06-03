# Three non-overlapping circles
#
# As a simple exercise in using the Turtle package you are
# required to draw three circles on the screen.  Each circle
# must be of a different size and colour.  Most importantly,
# the circles must not touch or overlap at any point, nor
# can one circle appear inside another.
#
# NB: We want unfilled circles, so you can't use Turtle's
# "dot" function for this purpose.  Also, you must ensure that
# lines are not drawn between or connecting the circles.
#
# The basic strategy for drawing each circle is to lift
# up the pen, move to a suitable location on the screen,
# choose a colour, put the pen down and walk in a circle.
# Having done this once you can copy your code (with minor
# changes) three times.
#
# Observation: Turtle's "circle" function does NOT draw a
# circle centred at the current location.  Instead it causes
# the turtle to walk in a circle, ending up back where
# it started.

from turtle import *
import turtle

setup()
title('Three non-overlapping circles')

## PUT YOUR CODE HERE
from random import randint
import random
turtle.speed("fastest")

a_color = ["blue", "red", "yellow", "green", "orange"]
tally = 0

for circles in range(5000):
    x_coord = randint(-200, 200)
    y_coord = randint(-200, 200)
    penup()
    goto(x_coord, y_coord)
    pendown()
    radius = randint(25, 100)
    a_fill_color = random.choice(a_color)
    fillcolor(a_fill_color)
    pendown()
    begin_fill()
    circle(radius)
    penup()
    end_fill()
    forward(200)                       
    if a_fill_color == 'red':
        tally = tally + 1
    
print(tally)
hideturtle()
done()
