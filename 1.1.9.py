#1.1.9 AP Exam Practice
import turtle as trtl
painter = trtl.Turtle()
mtlist = []
x = 270
y = int(input("enter a number "))
z = y
painter.penup()
painter.goto(-250,0)
painter.pendown()
while y > 0:
  mtlist.append(y)
  y = y - 1
print(mtlist)
if z > 8:
  painter.pencolor("green")
  painter.pensize(10)
else:
  painter.pencolor("red")
  painter.pensize(5)
for number in mtlist:
  x = x + (360/z)
  #painter.circle(25)
  painter.setheading(x)
  painter.forward(100)



wn = trtl.Screen()
wn.mainloop()