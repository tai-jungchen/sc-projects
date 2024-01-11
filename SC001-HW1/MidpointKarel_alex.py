from karel.stanfordkarel import *

"""
File: MidpointKarel.py
Name: Vivian Lin
----------------------------
When you finish writing it, MidpointKarel should
leave a beeper on the corner closest to the center of 1st Street
(or either of the two central corners if 1st Street has an even
number of corners).  Karel can put down additional beepers as it
looks for the midpoint, but must pick them up again before it
stops.  The world may be of any size, but you are allowed to
assume that it is at least as tall as it is wide.
"""


def main():
    """
    TODO:
    """
    while front_is_clear():
        move()
        turn_left()
        go_two_steps()
        if front_is_clear():
            turn_right()
    if not front_is_clear():
        turn_around()
    while front_is_clear():
        move()
    put_beeper()


def turn_around():
    for i in range(2):
        turn_left()


def go_two_steps():
    for i in range(2):
        if front_is_clear():
            move()


def turn_right():
    for i in range(3):
        turn_left()


# DO NOT EDIT CODE BELOW THIS LINE #


if __name__ == '__main__':
    execute_karel_task(main)
