"""
File: complement.py
Name:Vivian Lin
----------------------------
This program uses string manipulation to
tackle a real world problem - finding the
complement strand of a DNA sequence.
THe program asks uses for a DNA sequence as
a python string that is case-insensitive.
Your job is to output the complement of it.
"""


def main():
    """
    This function is to find the complement sequence of certain DNA sequence.
    """
    dna = input("Give me DNA: ")
    dna = dna.upper()
    new_dna = input("The complement of "+str(dna) + " is "+str(build_complement(dna)))


def build_complement(dna):
    ans = ""
    for ch in dna:
        if ch == "A":
            ans += "T"
        elif ch == "T":
            ans += "A"
        elif ch == "C":
            ans += "G"
        elif ch == "G":
            ans += "C"
    return ans


###### DO NOT EDIT CODE BELOW THIS LINE ######
if __name__ == '__main__':
    main()
