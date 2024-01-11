"""
File: sierpinski.py
Name: 
---------------------------
This file recursively prints the Sierpinski triangle on GWindow.
The Sierpinski triangle is a fractal described in 1915 by Waclaw Sierpinski.
It is a self similar structure that occurs at different levels of iterations.
"""

from campy.graphics.gwindow import GWindow
from campy.graphics.gobjects import GLine
from campy.gui.events.timer import pause

# Constants
ORDER = 3                  # Controls the order of Sierpinski Triangle
LENGTH = 600               # The length of order 1 Sierpinski Triangle
UPPER_LEFT_X = 150		   # The upper left x coordinate of order 1 Sierpinski Triangle
UPPER_LEFT_Y = 100         # The upper left y coordinate of order 1 Sierpinski Triangle
WINDOW_WIDTH = 950         # The width of the GWindow
WINDOW_HEIGHT = 700        # The height of the GWindow

# Global Variable
window = GWindow(width=WINDOW_WIDTH, height=WINDOW_HEIGHT)  # The canvas to draw Sierpinski Triangle


def main():
	"""
	TODO:
	"""
	sierpinski_triangle(ORDER, LENGTH, UPPER_LEFT_X, UPPER_LEFT_Y)


def sierpinski_triangle(order, length, upper_left_x, upper_left_y):
	"""
	:param order:
	:param length:
	:param upper_left_x:
	:param upper_left_y:
	:return:
	"""
	xy_pairs = [(upper_left_x, upper_left_y),
				 (upper_left_x + length / 2 * 0.5, upper_left_y + length / 2 * 0.866),
				 (upper_left_x + length / 2, upper_left_y)]
	if order == 1:
		pass
	else:
		for xy_pair in xy_pairs:
			x, y = xy_pair

			line_1 = GLine(x, y, x + length / 2, y)
			window.add(line_1)
			line_2 = GLine(x, y, x + length / 2 * 0.5, y + length / 2 * 0.866)
			window.add(line_2)
			line_3 = GLine(x + length / 2 * 0.5, y + length / 2 * 0.866, x + length / 2, y)
			window.add(line_3)
			pause(1000)
			sierpinski_triangle(order - 1, length / 2, x, y)


if __name__ == '__main__':
	main()