# author: tornado2
import turtle
akshar = turtle.Turtle()
sides = 6
length = 100
angle = 180 - 180 * (sides - 2)/sides

colors = ["red","orange","yellow","green","blue","purple"]

for color in colors:
	akshar.color(color)
	akshar.forward(length)
	akshar.right(angle)
