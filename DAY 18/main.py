from turtle import Turtle, Screen
import random
import colorgram

ninja = Turtle()
screen = Screen()

# sets the turtle on lower left
screen.setworldcoordinates(-1, -1, screen.window_width() - 1, screen.window_height() - 1)

# maximize window
screenTk = screen.getcanvas().winfo_toplevel()

try:
    screenTk.attributes("-zoom", 1)
except:
    screenTk.attributes("-fullscreen", 1)

screen.colormode(255)

ninja.shape("turtle")
ninja.color("black")
ninja.speed(10)


# draw square
# for _ in range(4):
#     ninja.forward(100)
#     ninja.right(90)
# --------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------


# draw dash-line      
# for i in range(15):
#     if i % 2 == 0:
#         ninja.pendown()
#     else:
#         ninja.penup()
        
#     ninja.forward(10)
# --------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------


# draw triangle, square, pentagon, hexagon, heptagon, octagon, nonagon, decagon
# sides = [3, 4, 5, 6, 7, 8, 9, 10]

# for s in sides:
    
#     angle = 360 / s
#     ninja.pencolor(random.randint(0,255), random.randint(0,255), random.randint(0,255))
    
#     for l in range(s):
#         ninja.forward(100)
#         ninja.right(angle)
# --------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------


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
# --------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------    


# # draw a spirograph
# total_circle = 5
# circle_diameter = 50
# angle = 360 / total_circle
# for i in range(total_circle):
#     ninja.pencolor(random.randint(0,255), random.randint(0,255), random.randint(0,255))
#     ninja.circle(circle_diameter)
#     ninja.right(angle)
# --------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------


color_list = []
# getting colors from 'colorgram'
# extracted_color = colorgram.extract('spot_painting.jpg', 30)

# for color in extracted_color:
#     color_list.append((color.rgb.r, color.rgb.g, color.rgb.b))

# print(color_list)

color_list = [(218, 165, 82), (82, 104, 151), (109, 154, 200), (243, 237, 225), (69, 127, 97), (129, 23, 61), (110, 173, 133), (158, 47, 81), (215, 202, 135), (152, 160, 53), (202, 116, 162), (239, 246, 243), (191, 69, 42), (36, 38, 81), (122, 116, 165), (205, 100, 54), (197, 83, 101), (87, 161, 117), (37, 49, 94), (73, 139, 180), (85, 24, 45), (220, 176, 197), (178, 187, 213), (173, 203, 186), (220, 179, 170), (81, 82, 27), (118, 34, 30), (92, 23, 17)]

total_row = 10
total_col = 10

per_row = (list(screen.screensize())[1] / total_row)
per_col =  (list(screen.screensize())[0] / total_col)

ninja.penup()
ninja.setpos(per_row, per_col)

for i in range(total_row):
    # ninja.setx(per_col)
    ninja.sety(per_row * i)
    for j in range(total_col):
        ninja.setx(per_col * j)
        ninja.dot(20, random.choice(color_list))

ninja.setx(ninja.xcor() + (per_row))
ninja.left(90)

screen.exitonclick()