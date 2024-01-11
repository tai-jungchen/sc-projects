from karel.stanfordkarel import *

"""
File: StoneMasonKarel.py
Name: Vivian Lin
--------------------------------
At present, the StoneMasonKarel file does nothing.
Your job in the assignment is to add the necessary code to
instruct Karel to build a column (a vertical structure
that is 5 beepers tall) in each avenue that is either on the right
or left side of the arch, as described in the Assignment 1 handout. 
Karel should end on the last avenue, 1st Street, facing east. 
"""


def main():
    """
    This function navigates karel to repair the damaged pillars.
    Pre-condition:karel is at the starting point and facing East.
    Post-condition:karel is at the termination and facing East.
    """
    while front_is_clear():
        turn_left()
        repair()
        turn_down()
        if not on_beeper():
            put_beeper()
        go_to_the_new_start_point()
    turn_left()
    repair()
    turn_down()
    if not on_beeper():
        put_beeper()
    go_down()
    turn_left()


def go_down():
    """
    This function indicates karel that it can move toward the ground without hitting it.
    Pre-condition:karel is facing the arch.
    Post-condition:karel is leaving the arch.
    """
    while front_is_clear():
        move()


def go_to_the_new_start_point():
    """
    This function instructs karel to move to the new pillar which is ready to be repaired.
    Pre-condition:karel is leaving the arch.
    Post-condition:karel is at the bottom of the arch and facing East.
    """
    while front_is_clear():
        move()
    turn_left()
    for i in range(4):
        move()


def repair():
    """
    This function informs karel to fill in the beeper into the places which originally without beeper.
    Pre-condition:karel is at the bottom of the arch and facing North.
    Post-condition:karel is at the highest of the arch and facing North.
    """
    while front_is_clear():
        if on_beeper():
            move()
        else:
            put_beeper()


def turn_down():
    """
    This function tells karel to turn 180 degrees.
    Pre-condition:karel is at the highest of the arch and facing North.
    Post-condition:karel is at the highest of the arch and facing South.
    """
    for i in range(2):
        turn_left()




# DO NOT EDIT CODE BELOW THIS LINE #

if __name__ == '__main__':
    execute_karel_task(main)
