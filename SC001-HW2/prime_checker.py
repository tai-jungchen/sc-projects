"""
File: prime_checker.py
Name:Vivian Lin
-----------------------
This program asks our user for input and checks if the input is a
prime number or not. First, ” Welcome to the prime checker” will be printed on Console.
And the program will continually ask the user to enter an integer 
that is greater than 1 and checks if it is a prime number.
The program ends when the user enter the EXIT number.
"""
EXIT = -100


def main():
	"""
	TODO:
	"""
	print("Welcome to the prime checker!")
	while True:
		n = int(input("n: "))
		if 	n == EXIT:
			print("Have a good one!")
		elif n == 2:
			print(str(n) + " is a prime number")
		elif n % 2 == 0:
			print(str(n)+" isn't a prime number")
		elif n == 3:
			print(str(n) + " is a prime number")
		elif n % 3 == 0:
			print(str(n) + " isn't a prime number")
		else:
			print(str(n) + " is a prime number")







###### DO NOT EDIT CODE BELOW THIS LINE ######

if __name__ == "__main__":
	main()
