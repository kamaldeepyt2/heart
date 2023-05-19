import turtle

turtle.speed(3)
turtle.bgcolor('black')
# turtle.pensize(10)

#function for curve....
def func():
    for i in range(200):
        turtle.right(1)
        turtle.forward(1)

turtle.color('white','red')

# function start for heart....
turtle.begin_fill()
turtle.pensize(3)

turtle.left(140)
turtle.forward(111.65)

func()
turtle.left(120)
func()

turtle.forward(111.65)
turtle.end_fill()

# function start for heart arrow....
turtle.right(80)
turtle.forward(70)

turtle.begin_fill()
turtle.pensize(8)

turtle.left(80)
turtle.forward(60)
turtle.right(180)
turtle.forward(280)

# turtle.color('white')
turtle.left(140)
turtle.forward(20)
turtle.backward(20)
turtle.right(280)
turtle.forward(20)
turtle.backward(20)
turtle.end_fill()

turtle.hideturtle()
turtle.done()
