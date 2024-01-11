"""
File: blur.py
Name: Ron Ron
-------------------------------
This file shows the original image first,
smiley-face.png, and then compare to its
blurred image. The blur algorithm uses the
average RGB values of a pixel's nearest neighbors.
"""

from simpleimage import SimpleImage


def blur(img):
    """
    :param img: the image that needs to be blurred
    :return: The blurred image
    """
    new_img = SimpleImage.blank(img.width, img.height)
    for x in range(4):
        for y in range(4):
            print("xy center point", x, ", ", y)
            pixel_to_fill = new_img.get_pixel(x, y)
            computed_red = 0
            computed_green = 0
            computed_blue = 0
            neighbor_counter = 0

            for hori in range(-1, 2):
                for verti in range(-1, 2):
                    print("x coord: ", x + hori, "y coord: ", y + verti)
                    if (x + hori >= 0) and (y + verti >= 0) and (x + hori < img.width) and (y + verti < img.height):
                        neighbor_pixel = img.get_pixel(x + hori, y + verti)
                        computed_red += neighbor_pixel.red
                        computed_green += neighbor_pixel.green
                        computed_blue += neighbor_pixel.blue
                        neighbor_counter += 1
            print("number of neighbors (including self):", neighbor_counter)
            print()

            pixel_to_fill.red = computed_red // neighbor_counter
            pixel_to_fill.green = computed_green // neighbor_counter
            pixel_to_fill.blue = computed_blue // neighbor_counter
    return new_img


def main():
    """
    TODO:
    """
    old_img = SimpleImage("images/smiley-face.png")
    old_img.show()

    blurred_img = blur(old_img)
    for i in range(1):      # change blurring times
        blurred_img = blur(blurred_img)
    blurred_img.show()


# ---- DO NOT EDIT CODE BELOW THIS LINE ---- #

if __name__ == '__main__':
    main()
