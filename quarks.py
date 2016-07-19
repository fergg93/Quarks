#  File: Mondrian.py

#  Description: Draws abstract art

#  Student Name: Fernando Garcia (id #: 40)

#  Student UT EID: fg4877

#  Course Name: CS 313E

#  Unique Number: 51730

#  Date Created: 03/07/15

#  Date Last Modified: 03/07/15



"Quarks"
#by Fernando Garcia

#This is it, the end of the road,
#red, green and blue is all I see,
#the foundation, the cosmological code,
#a sea of quarks surrounding me


import turtle

import random

import math


# recursive code to draw recursive circles
def recursion(ttl,radius,heading,level):
  ttl.penup()
  ttl.speed(0)
  ttl.width(0)
  circles=random.randint(2,5)
  if level==0:              # Base case
    return
  else:
    ttl.setheading(heading)
    ttl.penup()
    ttl.forward(radius)
    ttl.setheading(0)
    for i in range (circles):
      x=ttl.position()[0]
      y=ttl.position()[1]
      #Assign color
      rand=random.randint(0,2)
      if rand==0:
        color='steel blue'
      elif rand==1:
        color='tomato'
      else:
        color='medium sea green'
      ttl.penup()
      ttl.setheading(i*360/circles)
      ttl.pendown()
      ttl.color(color,color)
      ttl.begin_fill()
      ttl.width(0)
      ttl.circle(radius/2)
      ttl.end_fill()
      heading=(i*360/circles+90)
      recursion(ttl,radius/2,heading,level-1)
      ttl.goto(x,y)


def main():
  print("Mondrian composition")
  print()
  level=int(input("Enter a level of recursion between 1 and 6: "))

  # put label on top of page
  turtle.title ('Abstract')

  # setup screen size
  turtle.setup (800, 800, 0, 0)

  # create turtle object
  ttl = turtle.Turtle()

  # set line thickness
  ttl.width(0)

  #Draw initial circle
  ttl.penup()
  ttl.goto(0,-250)
  ttl.speed(0)
  ttl.pendown()
  #assign color
  rand=random.randint(0,2)
  if rand==0:
    color='steel blue'
  elif rand==1:
    color='tomato'
  else:
    color='medium sea green'
  ttl.color(color,color)
  ttl.begin_fill()
  ttl.circle(250)
  ttl.end_fill()


# Begin recursion
  radius=250
  recursion(ttl,radius,90,level)


  # hide the turtle
  ttl.hideturtle()

  #Save eps file
  ts = turtle.getscreen()
  ts.getcanvas().postscript(file = "Mondrian.eps")

  # persist the drawing
  turtle.done()

main()