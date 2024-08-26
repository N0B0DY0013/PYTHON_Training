# --------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

from turtle import Turtle, Screen
import random

ninja = Turtle()
screen = Screen()
screen.colormode(255)

ninja.shape("turtle")
ninja.color("chartreuse2")
ninja.speed(10)

# draw square
# for _ in range(4):
#     ninja.forward(100)
#     ninja.right(90)


# draw dash-line      
# for i in range(15):
#     if i % 2 == 0:
#         ninja.pendown()
#     else:
#         ninja.penup()
        
#     ninja.forward(10)


# draw triangle, square, pentagon, hexagon, heptagon, octagon, nonagon, decagon
# sides = [3, 4, 5, 6, 7, 8, 9, 10]

# for s in sides:
    
#     angle = 360 / s
#     ninja.pencolor(random.randint(0,255), random.randint(0,255), random.randint(0,255))
    
#     for l in range(s):
#         ninja.forward(100)
#         ninja.right(angle)


# draw random walk
# ninja.pensize(10)

# for _ in range(200):

#     ninja.pencolor(random.randint(0,255), random.randint(0,255), random.randint(0,255))
    
#     v_pos = random.randint(1,2)
#     h_pos = random.randint(1,2)
    
#     if h_pos == 1:
#         ninja.right(90)
#     else:
#         ninja.left(90)
        
#     if v_pos == 1:
#         ninja.forward(30)
#     else:
#         ninja.backward(30)
    

# draw a spirograph
for i in range(361):
    ninja.setheading(i)
    ninja.tiltangle(i+1*20)
    ninja.circle(50)
    #ninja.forward(i)




screen.exitonclick()