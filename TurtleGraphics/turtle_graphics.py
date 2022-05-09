# Aidan Henry
# turtle graphics program

import random
import time
from turtle import Turtle

def recursive_donut(turtle, angle, quantity, delta, radius):
    colors = ["red", "orange", "brown", "green", "blue", "purple"]
    color = random.choice(colors)
    turtle.color(color)
    turtle.right(angle)
    turtle.forward(delta)
    unit_angle = 360.0/quantity
    for x in range(quantity):
        turtle.circle(radius)
        turtle.forward(90)
        turtle.left(300)
        turtle.left(unit_angle)
    radius = radius - delta
    if (radius > 5):
        recursive_donut(turtle, angle, quantity, delta, radius)

def main():
    animation_speed = 0
    leonardo = Turtle()
    donatello = Turtle()
    donatello.speed(animation_speed)
    leonardo.speed(animation_speed)
    recursive_donut(leonardo, 10, 15, 5, 100)
    recursive_donut(donatello, 2, 45, 5, 100)
    time.sleep(20)

main()
