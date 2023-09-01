# turtle party project
# by Priscilla Schwartz
# 9/1/23

import turtle
turtle.color ("red")

def back (len):
  turtle.penup ()
  turtle.backward (len)
  turtle.pendown ()
  
def polygon (num, size):
  for i in range (num):
    turtle.forward (size)
    turtle.left (350/num)
    
polygon (4,100)
back (125)
polygon (3,50)
