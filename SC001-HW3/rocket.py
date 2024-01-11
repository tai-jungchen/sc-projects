"""
File: rocket.py
Name:Vivian Lin
-----------------------
This program should implement a console program
that draws ASCII art - a rocket.
The size of rocket is determined by a constant
defined as SIZE at top of the file.
Output format should match what is shown in the sample
run in the Assignment 2 Handout.

"""

# This constant determines rocket size.
SIZE = 10


def main():
	"""
	This function is to build the rocket in any size.
	"""
	head()
	belt()
	upper()
	lower()
	belt()
	head()


def head():
	"""
	This function is to build the head of the rocket in any size.
	"""
	for i in range(SIZE):
		count = 0
		for j in range(SIZE*2+1):
			if j == 0:
				print(" ", end="")
			if j < SIZE:
				if (i+j) < (SIZE-1):
					print(" ", end="")
				else:
					print("/", end="")
					count += 1
		for k in range(count):
			print("\\", end="")
		print("")


def belt():
	"""
	This function is to build the belt of the rocket in any size.
	"""
	for i in range(1):
		for j in range(SIZE*2+1):
			if (i+j) == 0:
				print("+", end="")
			if (i+j) == (SIZE*2):
				print("+", end="")
			else:
				print("=", end="")
		print("")


def upper():
	"""
	This function is to build the upper body of the rocket in any size.
	"""
	for i in range(SIZE):
		for j in range(SIZE*2+2):
			if j == 0 or j == (SIZE*2+1):
				print("|", end="")
			elif (i+j) <= (SIZE-1):
				print(".", end='')
			elif (i+j) >= (SIZE*3-2*(SIZE-i-1)):
				print(".", end='')
			elif (i+j+SIZE) % 2 == 0:
				print("/", end="")
			elif (i+j+SIZE) % 2 == 1:
				print("\\", end="")
		print("")


def lower():
	"""
	This function is to build the lower body of the rocket in any size.
	"""
	for i in range(SIZE):
		for j in range(SIZE*2+2):
			if j == 0 or j == (SIZE * 2 + 1):
				print("|", end="")
			elif (i+j) >= (SIZE*2+1):
				print(".", end='')
			elif j <= i:
				print(".", end='')
			elif (i+j) % 2 == 0:
				print("/", end="")
			elif (i+j) % 2 == 1:
				print("\\", end="")
		print("")














###### DO NOT EDIT CODE BELOW THIS LINE ######

if __name__ == "__main__":
	main()