"""
File: similarity.py
Name:
----------------------------
This program compares short dna sequence, s2,
with sub sequences of a long dna sequence, s1
The way of approaching this task is the same as
what people are doing in the bio industry.
"""


def main():
    """
    This function is to find the most similar DNA fragrance in certain DNA sequence by
    comparing the DNA which we would like to match to certain DNA sequence.
    """
    long_sequence = input("Please give me a DNA sequence to search: ")
    long_sequence = long_sequence.upper()
    short_sequence = input("What DNA sequence would you like to match? ")
    fragrance_sequence = input("The best match is " +str(find_the_best_match(long_sequence)))


def find_the_best_match(long_sequence):
    ans = ""
    for i in range(long_sequence):
        pass


###### DO NOT EDIT CODE BELOW THIS LINE ######
if __name__ == '__main__':
    main()
