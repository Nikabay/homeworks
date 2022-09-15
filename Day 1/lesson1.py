from turtle import *

#we want to paint a house


#drawing a square
shape("turtle")
speed(30)
width(7)
color("purple")
forward(200)
left(90)

forward(200)
left(90)

forward(200)
left(90)

forward(200)
left(90)
#end of square

#drawing a door
forward(70)
color("yellow")
begin_fill()
left(90)
forward(120) #height of the door
right(90)
forward(60)
right(90)
forward(120)
end_fill()
#end of door

#drawing a roof
penup()
goto(200, 200)
pendown()

color("red")
begin_fill()
right(150)
forward(200)
left(120)
forward(200)
end_fill()
#end of roof

#drawing a left window
penup()
goto(0, 0)
right(150)

goto(30, 0)
forward(150)
pendown()

color("green")
begin_fill()

forward(35)
right(90)
forward(35)
right(90)
forward(35)
right(90)
forward(35)
end_fill()
#end of left window

#drawing a right window
penup()
goto(200, 0)
right(90)

goto(170, 0)
forward(150)
pendown()

color("green")
begin_fill()

forward(35)
left(90)
forward(35)
left(90)
forward(35)
left(90)
forward(35)
end_fill()
#end of rightt window

print("nika sagol")

exitonclick()
