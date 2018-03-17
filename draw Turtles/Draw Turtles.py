import turtle

def draw_square():
    brad=turtle.Turtle()
    brad.shape("circle")
    brad.color("yellow")
    brad.speed(2)
    i=1
    while i<=4:
        brad.forward(100)
        brad.right(90)
        i+=1

def draw_cirlce():
    angie = turtle.Turtle()
    angie.shape("arrow")
    angie.color("blue")
    angie.circle(100)

def draw_triangle():
    tri = turtle.Turtle()
    tri.shape("turtle")
    tri.color("white")
    i=1
    while i<=2:
        tri.forward(100)
        tri.left(120)
        i+=1
    tri.forward(100)

def draw_art():

    ceta=0
    while ceta<360:
        brad = turtle.Turtle()
        brad.shape("turtle")
        brad.color("yellow")
        brad.speed(5)
        i=1
        brad.right(ceta)
        while i<=4:
            brad.forward(100)
            brad.right(90)
            i+=1
        ceta+=10


window=turtle.Screen()
window.bgcolor("red")
# draw_cirlce()
# draw_square()
# draw_cirlce()
# draw_triangle()
# draw_cirlce()

draw_art()


window.exitonclick()

#https://www.youtube.com/watch?v=1cM05mJK4JQ
#sudo apt-get install python-tk
#https://stackoverflow.com/questions/4783810/install-tkinter-for-python
#https://docs.python.org/2/library/turtle.html#turtle.speed
#https://docs.python.org/2/library/turtle.html#turtle.color
#https://docs.python.org/2/library/turtle.html#turtle.shape
#https://docs.python.org/2/library/turtle.html
#https://www.youtube.com/watch?time_continue=1&v=P2wRyGo_xXA
#https://youtu.be/4Ea22iSyAK4