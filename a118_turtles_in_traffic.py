#   a118_turtles_in_traffic.py
#   Move turtles horizontally and vertically across screen.
#   Stopping turtles when they collide.
import turtle as trtl

# create two empty lists of turtles, adding to them later
horiz_turtles = []
vert_turtles = []

# use interesting shapes and colors
turtle_shapes = ["arrow", "turtle", "circle", "square", "triangle", "classic"]
horiz_colors = ["red", "blue", "green", "orange", "purple", "gold"]
vert_colors = ["darkred", "darkblue", "lime", "salmon", "indigo", "brown"]

tloc = 50
for s in turtle_shapes:
  #initializes turtle object type 1, places it and sets heading to 0
  ht = trtl.Turtle(shape=s)
  horiz_turtles.append(ht)
  ht.penup()
  new_color = horiz_colors.pop()
  ht.fillcolor(new_color)
  ht.goto(-350, tloc)
  ht.setheading(0)
  #initializes turtle object type 2, places it and sets heading to 270
  vt = trtl.Turtle(shape=s)
  vert_turtles.append(vt)
  vt.penup()
  new_color = vert_colors.pop()
  vt.fillcolor(new_color)
  vt.goto( -tloc, 350)
  vt.setheading(270)
  # adds 50 to tloc so the y of the turtle increase by 0 each time the loop iterates
  tloc += 50

# TODO: move turtles across and down screen, stopping for collisions

for step in range(50):
  if abs(ht.xcor() - vt.xcor()) <=20:
    horiz_turtles.pop(0)
  if abs(ht.ycor() - vt.xcor()) <=20:
    vert_turtles.pop(0)

    
  for h in horiz_turtles:
    h.forward(10)
  for v in vert_turtles:
      v.forward(10)


wn = trtl.Screen()
wn.mainloop()