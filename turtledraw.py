# author: tornado2
import turtle
akshar = turtle.Turtle()
sides = 150
length = 10
angle = 180 - 180 * (sides - 2)/sides
numbers = range(0,sides)
colors = ["red","orange","yellow","green","blue","purple"]
for number in numbers:
	for color in colors:
		akshar.color(color)
		akshar.forward(length)
		akshar.right(angle +200)
	
	


