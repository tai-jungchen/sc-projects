from karel.stanfordkarel import *

"""
File: CollectNewspaperKarel.py
Name: Vivian Lin
--------------------------------
At present, the CollectNewspaperKarel file does nothing.
Your job in the assignment is to add the necessary code to
instruct Karel to walk to the door of its house, pick up the
newspaper (represented by a beeper, of course), and then return
to its initial position in the upper left corner of the house.
"""


def main():
    """
    This function navigates karel to pick up the newspaper and go back to its original position.
    Pre-condition:karel is at the north-west of the house.
    """
    move_to_newspaper()
    take_newspaper_home_and_read()


def take_newspaper_home_and_read():
    """
    Pre-condition:karel is on the newspaper.
    Post-condition:karel is at the north-west of the house.
    """
    pick_beeper()
    for i in range(2):
        turn_left()
    while front_is_clear():
        move()
    turn_right()
    move()
    turn_right()
    put_beeper()


def move_to_newspaper():
    """
    Pre-condition:karel is at the north-west of the house.
    Post-condition:karel is on the newspaper.
    """
    while front_is_clear():
        move()
    turn_right()
    move()
    turn_left()
    move()


def turn_right():
    for i in range(3):
        turn_left()


# DO NOT EDIT CODE BELOW THIS LINE #

if __name__ == '__main__':
    execute_karel_task(main)
