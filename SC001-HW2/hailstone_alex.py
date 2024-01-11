"""
File: hailstone.py
Name:Vivian Lin
-----------------------
This program should implement a console program that simulates
the execution of the Hailstone sequence, defined by Douglas
Hofstadter. Output format should match what is shown in the sample
run in the Assignment 2 Handout.
"""


def main():
    """
    TODO:
    """
    print("This program computes Hailstone sequences.")
    n = int(input("Enter a number: "))
    counter = 0

    while True:
        if n == 1:
            print("It took " + str(counter) + " steps to reach 1.")
            break
        elif n % 2 == 1:
            print(str(n)+" is odd, so I make 3n+1: "+str(3 * n + 1))
            n = 3 * n + 1
        elif n % 2 == 0:
            print(str(n) + " is even, so I make half: " + str(n // 2))
            n = n // 2
        counter += 1


###### DO NOT EDIT CODE BELOW THIS LINE ######

if __name__ == "__main__":
    main()
