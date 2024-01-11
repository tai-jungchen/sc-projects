"""
File: coin_flip_runs.py
Name: Ron Ron
-----------------------
This program should simulate coin flip(s)
with the number of runs input by users.
A 'run' is defined as consecutive results
on either 'H' or 'T'. For example, 'HHHHHTHTT'
is regarded as a 2-run result.
Your program should stop immediately after your
coin flip results reach the number of runs!
"""

import random


def main():
	"""
	This function is to find out the result of the given times of getting continuous same side of coin
	in the coin flipping game.
	"""
	print("Let's flip a coin!")
	num_run = int(input("Number of runs: "))
	consec = False
	last_consec = False
	last_flip = -1
	end_run_counter = 0

	while True:
		# check end condition
		if end_run_counter == num_run:
			print("\nEnd game by runs")
			break

		# generate random flips
		flip = random.randint(0, 1)
		if flip == 1:
			print("H", end="")
		else:
			print("T", end="")

		# check consecutive or not
		if flip == last_flip:
			consec = True
		elif last_flip == -1:		# first flip
			consec = False
		else:
			consec = False
		last_flip = flip		# update flip

		# count runs
		if (last_consec == False) and (consec == True):
			end_run_counter += 1
		last_consec = consec		# update consec


# ---- DO NOT EDIT CODE BELOW THIS LINE ---- #
if __name__ == "__main__":
	main()
