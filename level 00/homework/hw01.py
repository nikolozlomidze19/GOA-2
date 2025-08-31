from turtle import*

#we want to paint a house

#step1: draw a square
shape("arrow")
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
# end of sqaure

# drawing a door
begin_fill()
forward(70)
color("yellow")
left(90)
forward(120) # height of the door
right(90)
forward(60)
right(90)
forward(120)
end_fill()

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

right(150)
left(180)
left(90)

penup()
goto(65, 140)
pendown()

color("brown")
begin_fill()
left(90)
forward(40)
left(90)
forward(40)
left(90)
forward(40)
left(90)
forward(40)
left(180)
end_fill()

penup()
goto(130,140)
pendown()


begin_fill()
right(90)
forward(40)
right(90)
forward(40)
right(90)
forward(40)
right(90)
forward(40)
end_fill()

exitonclick()