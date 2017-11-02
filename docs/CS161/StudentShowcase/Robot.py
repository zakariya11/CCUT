
import turtle
t = turtle.Turtle()
turtle.bgcolor("#FFFFFF")
t.color("#000000")
turtle.bgcolor('black')
colors = ['red', 'yellow', 'blue', 'green']
t.speed(7)
t.penup()
t.goto(0,260)
t.pendown()
t.pencolor('#00FFFF')
t.pensize(8)
t.forward(50)
t.left(90)
t.forward(80)
t.left(90)
t.forward(30)
t.right(150)
t.pensize(3)
t.forward(40)
t.backward(40)
t.pensize(8)
t.left(150)
t.forward(40)
t.right(30)
t.pensize(3)
t.forward(40)
t.backward(40)
t.left(30)
t.pensize(8)
t.forward(30)
t.left(90)
t.forward(80)
t.left(90)
t.forward(70)
t.penup()
t.goto(-35,310)
t.pendown()
t.left(20)
t.pensize(10)
t.forward(30)
t.penup()
t.goto(35,310)
t.pendown()
t.left(140)
t.pensize(10)
t.forward(30)
t.penup()
t.goto(0,290)
t.pendown()
t.pensize(3)
t.right(160)
t.right(90)
t.circle(10, 180)
t.penup()
t.goto(-20,290)
t.pendown()
t.right(90)
t.right(90)
t.circle(10, 180)

t.penup()
t.right(180)
t.goto(10,260)
t.pencolor('#FF69B4')
t.pendown()
t.pensize(4)
t.forward(40)
t.left(90)
t.forward(100)
t.right(90)
t.forward(75)
t.left(90)
t.forward(125)
t.right(90)
t.forward(200)
t.right(90)
t.forward(25)
t.right(90)
t.forward(175)
t.left(90)
t.forward(100)
t.left(90)
t.forward(120)
t.right(90)
t.forward(60)
t.left(90)
t.forward(175)
t.left(90)
t.forward(60)
t.right(90)
t.forward(25)
t.right(90)
t.forward(85)
t.right(90)
t.forward(175)
t.circle(25, 180)
t.forward(175)
t.right(90)
t.forward(85)
t.right(90)
t.forward(25)
t.right(90)
t.forward(60)
t.left(90)
t.forward(175)
t.left(90)
t.forward(60)
t.right(90)
t.forward(120)
t.left(90)
t.forward(125)
t.right(90)
t.forward(200)
t.right(90)
t.forward(25)
t.right(90)
t.forward(175)
t.left(90)
t.forward(100)
t.left(90)
t.forward(75)
t.right(90)
t.forward(100)
t.left(90)
t.forward(40)
t.penup()
t.goto(-222.5,322)
t.pendown()
t.pensize(7)
t.forward(40)
t.begin_fill()
t.fillcolor('red')
t.pencolor('red')
t.penup()
t.goto(100,150)
t.pendown()
t.circle(15,180)
t.penup()
t.goto(70,150)
t.pendown()
t.right(180)
t.circle(15,180)
t.left(30)
t.forward(60)
t.left(120)
t.forward(60)
t.end_fill()
t.speed('fastest')
t.penup()
t.goto(300,300)
t.pendown()
t.pensize(1)
for x in range(50):
    t.pencolor(colors[x%4])
    t.circle(x)
    t.left(91)
t.penup()
t.goto(-200,-200)
t.pendown()
for y in range(100):
    t.pencolor(colors[y%4])
    t.forward(y)
    t.left(91)
t.penup()
t.goto(300,-300)
t.pendown()
sides = 6
colorr = ['red', 'yellow', 'blue', 'orange', 'green', 'purple']
for z in range(50):
    t.pencolor(colorr[z%sides])
    t.forward(z * 3/sides +z)
    t.left(360/sides + 1)
    t.width(z*sides/200)
t.penup()
t.goto(-300,300)
t.pendown()
sides = 3
colorr = ['red', 'yellow', 'blue', 'orange', 'green', 'purple']
for k in range(50):
 t.pencolor(colorr[k%sides])
 t.forward(k * 3/sides +k)
 t.left(360/sides + 1)
 t.width(k*sides/200)

 turtle.exitonclick()