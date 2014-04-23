# author: tornado2
import turtle
akshar = turtle.Turtle()
sides = 5
length = 100
angle = 180 - 180 * (sides - 2)/sides
numbers = [ 1, 2, 3, 4, 5, 6 ]
for number in numbers:
	akshar.forward(length)
	akshar.right(angle)
