"""
File:draw_line.py
Name:Vivian Lin
-------------------------
TODO:
"""

from campy.graphics.gobjects import GOval, GLine
from campy.graphics.gwindow import GWindow
from campy.gui.events.mouse import onmouseclicked
SIZE = 5
window = GWindow()
counter = 0


def main():
    """
    This program creates lines on an instance of GWindow class.
    There is a circle indicating the user’s first click. A line appears
    at the condition where the circle disappears as the user clicks
    on the canvas for the second time.
    """
    if counter % 2 == 0:
        onmouseclicked(draw_oval)
    else:
        onmouseclicked(draw_line)


def draw_oval(mouse):
    oval = GOval(SIZE, SIZE, x=mouse.x, y=mouse.y)
    oval.filled = False
    window.add(oval)
    global counter
    counter += 1


def draw_line(mouse):
    line = GLine(x0=oval.x, y0=oval.y, x1=mouse.x, y1=mouse.y)
    window.add(line)
    global counter
    counter += 1


if __name__ == "__main__":
    main()
