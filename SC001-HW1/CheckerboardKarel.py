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
    # 8x1 and 1x1 cases
    if not front_is_clear():
        special_cases()
    # others
    else:
        while front_is_clear():
            left_to_right()
            if facing_west():
                right_to_left()
            go_to_next_level()


def left_to_right():
    put_beeper()
    while front_is_clear():
        move()
        if front_is_clear():
            move()
            put_beeper()
    # odd cases
    if on_beeper():
        turn_left()
        go_to_next_level()
    # even cases
    else:
        turn_left()
        go_to_next_level()
        if not facing_north():
            put_beeper()


def right_to_left():
    # odd cases
    if not on_beeper():
        while front_is_clear():
            move()
            put_beeper()
            if front_is_clear():
                move()
        turn_right()
    # even cases
    else:
        while front_is_clear():
            move()
            if front_is_clear():
                move()
                put_beeper()
        turn_right()


def go_to_next_level():
    if front_is_clear():
        move()
        if right_is_clear():
            turn_right()
        else:
            turn_left()


def special_cases():
    turn_left()
    put_beeper()
    while front_is_clear():
        move()
        if front_is_clear():
            move()
            put_beeper()


def turn_right():
    for i in range(3):
        turn_left()


# DO NOT EDIT CODE BELOW THIS LINE #

if __name__ == '__main__':
    execute_karel_task(main)
