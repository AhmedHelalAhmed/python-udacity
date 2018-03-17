import turtle
#https://www.youtube.com/watch?time_continue=10&v=4Ea22iSyAK4
def draw_art():

    ceta=0
    while ceta<360:
        tri = turtle.Turtle()

        tri.shape("turtle")
        tri.color("white")
        i = 1
        tri.left(ceta)
        while i <= 2:
            tri.forward(50)
            tri.left(20)
            i += 1
        tri.forward(-100)
        ceta+=10
    tri = turtle.Turtle()
    tri.shape("turtle")
    tri.color("white")
    tri.left(-90)
    tri.forward(150)

window=turtle.Screen()
window.bgcolor("red")



draw_art()


window.exitonclick()



#############
# import turtle
#
# def draw_art():
#
#     ceta=0
#     while ceta<3600:
#         tri = turtle.Turtle()
#         tri.right(ceta)
#         tri.shape("turtle")
#         tri.color("white")
#         i = 1
#         while i <= 2:
#             tri.forward(100)
#             tri.left(120)
#             i += 1
#         tri.forward(100)
#         ceta+=30
#
#
# window=turtle.Screen()
# window.bgcolor("red")
#
#
#
# draw_art()
#
#
# window.exitonclick()


###############
# import turtle
#
# def draw_art():
#
#     ceta=0
#     while ceta<3600:
#         tri = turtle.Turtle()
#         tri.right(ceta)
#         tri.shape("turtle")
#         tri.color("white")
#         i = 1
#         while i <= 2:
#             tri.forward(50)
#             tri.left(50)
#             i += 1
#         tri.forward(50)
#         ceta+=30
#
#
# window=turtle.Screen()
# window.bgcolor("red")
#
#
#
# draw_art()
#
#
# window.exitonclick()