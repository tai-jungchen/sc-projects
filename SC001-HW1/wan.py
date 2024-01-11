from karel.stanfordkarel import *

"""
File: CheckerboardKarel.py
Name: Vivian Lin
----------------------------
When you finish writing it, CheckerboardKarel should draw
a checkerboard using beepers, as described in Assignment 1. 
You should make sure that your program works for all of the 
sample worlds provided in the starter folder.
"""


def main():
    """
    TODO:
    """
    while front_is_clear():
        while front_is_clear():
            put_beeper()
            move()
            if front_is_clear():
                move()
                if not front_is_clear():
                    put_beeper()
        for i in range(2):
            turn_left()
        while front_is_clear():
            move()
        turn_right()
        if front_is_clear():
            move()
        turn_right()
        while front_is_clear():
            move()
            put_beeper()
            if front_is_clear():
                move()
        if not front_is_clear():
            for i in range(2):
                turn_left()
        while front_is_clear():
            move()
        turn_right()
        if front_is_clear():
            move()
        turn_right()


def turn_right():
    for i in range(3):
        turn_left()


# DO NOT EDIT CODE BELOW THIS LINE #

if __name__ == '__main__':
    execute_karel_task(main)
