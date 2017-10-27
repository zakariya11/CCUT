# RosettesAndPolygons.py

import turtle
t = turtle.Pen()
t.speed(20)          # Set turtle drawing speed

colors=['deep sky blue', 'orange red', 'sea green', 'dark slate gray', 'cyan', 'purple',
        'deep pink', 'navy', 'lavender', 'aquamarine', 'pink', 'gold']
sides = int(turtle.numinput("Number of sides", "How many spiral sides?", 4))

for m in range(5, 75):
    t.pencolor(colors[m % sides])
    t.left(360/sides + 5)
    t.width(m//25+1)        ## // is floor division
    t.penup()
    t.forward(m * 4)
    t.pendown()
    if (m % 2 == 0):     # Draw a rosette at each even corner
        for n in range(sides):
            t.circle(m/3)
            t.right(360/sides)
    else:                # Draw a polygon at each odd corner
        for n in range(sides):
            t.forward(m)
            t.right(360/sides)

turtle.exitonclick()
