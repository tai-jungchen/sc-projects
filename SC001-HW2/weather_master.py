"""
File: weather_master.py
Name:
-----------------------
This program should implement a console program
that asks weather data from user to compute the
average, highest, lowest, cold days among the inputs.
Output format should match what is shown in the sample
run in the Assignment 2 Handout.

"""
EXIT = -100


def main():
	"""
	TODO:
	"""
	print("stanCode \" Weather Master 4.0\"!")
	while True:
		n = int(input("Next Temperature: (or EXIT to quit)?"))
		if n == EXIT:
			print("No temperatures were entered.")
			break







###### DO NOT EDIT CODE BELOW THIS LINE ######

if __name__ == "__main__":
	main()
