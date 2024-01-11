"""
File: quadratic_solver.py
Name:
-----------------------
This program should implement a console program
that asks 3 inputs (a, b, and c)
from users to compute the roots of equation:
ax^2 + bx + c = 0
Output format should match what is shown in the sample
run in the Assignment 2 Handout.

"""

import math


def main():
	"""
	TODO:
	"""
	print("stanCode Quadratic Solver!")
	a = int(input("a= "))
	b = int(input("b= "))
	c = int(input("c= "))
	y = (b**2-4*a*c)
	if a == 0:
		print("Not a quadratic function")
	elif y > 0:
		x1 = (-b + math.sqrt(y)) / (2 * a)
		x2 = (-b - math.sqrt(y)) / (2 * a)
		print("Two roots: "+str(x1)+","+str(x2))
	elif y == 0:
		x1 = (-b ) / (2 * a)
		x2 = (-b ) / (2 * a)
		print("One roots: "+str(x1))
	else:
		print("No real roots")











###### DO NOT EDIT CODE BELOW THIS LINE ######

if __name__ == "__main__":
	main()
