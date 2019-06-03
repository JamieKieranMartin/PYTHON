
#-----Statement of Authorship----------------------------------------#
#
#  By submitting this task I agree that it represents my own work.
#  I am aware of the University rule that a student must not
#  act in a manner which constitutes academic dishonesty as stated
#  and explained in QUT's Manual of Policies and Procedures,
#  Section C/5.3 "Academic Integrity" and Section E/2.1 "Student
#  Code of Conduct".
#
#--------------------------------------------------------------------#



#-----Task Description-----------------------------------------------#




from turtle import *


# PUT YOUR CODE HERE
setup()
width(5)
speed("fast")

#Defines the code which draws a circle
def draw_a_circle():
    penup()
    forward(50)
    left(180)
    pendown()
    circle(50)
    penup()
    left(180)
    forward(50)

#Draw and colour the red square
pendown()    
fillcolor("red")
begin_fill()

for square in range(4):
    
    forward(200)
    left(90)
    
end_fill()

#Draw the circles and colours them.
#If the turtle has drawn two circles, then move to opposite side.
colours = ["#992BCC", "#000000", "#00FF00", "#000000"]
x = 0
while x < len(colours):
    fillcolor(colours[x])
    begin_fill()
    draw_a_circle()
    x += 1
    end_fill()
    if x == 2:
        left(90)
        forward(200)
        left(90)

hideturtle()
done()



