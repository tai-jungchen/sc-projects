"""
File: my_drawing.py
Name:Vivian Lin
----------------------
One of my most impressive view in my New York trip in 2021.
"""

from campy.graphics.gobjects import GOval, GRect, GPolygon, GArc, GLine, GLabel
from campy.graphics.gwindow import GWindow


def main():
    """
    This function create the image of the Empire State Building.
    """
    window = GWindow(width=800, height=800)

    back = GRect(800, 800)
    back.filled = True
    back.fill_color = "lightskyblue"
    back.color = "lightskyblue"
    window.add(back)

    tip = GOval(4, 4, x=window.width / 2 - 2, y=26)
    tip.filled = True
    tip.fill_color = "red"
    tip.color = "red"
    window.add(tip)

    top_four = GRect(2, 80, x=window.width / 2 - 1, y=30)
    top_four.filled = True
    top_four.fill_color = "lightgray"
    top_four.color = "lightgray"
    window.add(top_four)

    top_three = GRect(20, 30, x=window.width / 2 - 10, y=110)
    top_three.filled = True
    top_three.fill_color = "lightgray"
    top_three.color = "lightgray"
    window.add(top_three)

    top_two = GRect(30, 60, x=window.width / 2 - 15, y=130)
    top_two.filled = True
    top_two.fill_color = "lightgray"
    top_two.color = "lightgray"
    window.add(top_two)

    top_one = GRect(60, 10, x=window.width / 2 - 30, y=190)
    top_one.filled = True
    top_one.fill_color = "lightgray"
    top_one.color = "lightgray"
    window.add(top_one)

    head_two = GRect(60, 40, x=window.width / 2 - 30, y=200)
    head_two.filled = True
    head_two.fill_color = "gray"
    head_two.color = "gray"
    window.add(head_two)

    head_one = GRect(80, 60, x=window.width / 2 - 40, y=240)
    head_one.filled = True
    head_one.fill_color = "dimgray"
    head_one.color = "dimgray"
    window.add(head_one)

    main_body = GRect(100, 300, x=window.width/2-50, y=300)
    main_body.filled = True
    main_body.fill_color = "dimgray"
    main_body.color = "dimgray"
    window.add(main_body)

    waist_one = GRect(140, 30, x=window.width/2-70, y=600)
    waist_one.filled = True
    waist_one.fill_color = "dimgray"
    waist_one.color = "dimgray"
    window.add(waist_one)

    waist_two = GRect(150, 70, x=window.width / 2 - 75, y=630)
    waist_two.filled = True
    waist_two.fill_color = "dimgray"
    waist_two.color = "dimgray"
    window.add(waist_two)

    base_one = GRect(200, 70, x=window.width / 2 - 100, y=700)
    base_one.filled = True
    base_one.fill_color = "dimgray"
    base_one.color = "dimgray"
    window.add(base_one)

    base_two = GRect(300, 30, x=window.width / 2 - 150, y=770)
    base_two.filled = True
    base_two.fill_color = "dimgray"
    base_two.color = "dimgray"
    window.add(base_two)

    base_three = GRect(400, 10, x=window.width / 2 - 200, y=790)
    base_three.filled = True
    base_three.fill_color = "black"
    base_three.color = "black"
    window.add(base_three)

    decoration_one = GRect(40, 360, x=window.width / 2 - 20, y=240)
    decoration_one.filled = True
    decoration_one.fill_color = "darkgray"
    decoration_one.color = "darkgray"
    window.add(decoration_one)

    decoration_two = GRect(4, 300, x=window.width / 2 - 20, y=300)
    decoration_two.filled = True
    decoration_two.fill_color = "black"
    decoration_two.color = "black"
    window.add(decoration_two)

    decoration_three = GRect(4, 60, x=window.width / 2 - 22, y=240)
    decoration_three.filled = True
    decoration_three.fill_color = "black"
    decoration_three.color = "black"
    window.add(decoration_three)

    decoration_four = GRect(20, 30, x=window.width / 2 + 50, y=600)
    decoration_four.filled = True
    decoration_four.fill_color = "darkgray"
    decoration_four.color = "darkgray"
    window.add(decoration_four)

    decoration_five = GRect(4, 30, x=window.width / 2 + 50, y=600)
    decoration_five.filled = True
    decoration_five.fill_color = "black"
    decoration_five.color = "black"
    window.add(decoration_five)

    decoration_six = GRect(40, 140, x=window.width / 2 - 20, y=630)
    decoration_six.filled = True
    decoration_six.fill_color = "darkgray"
    decoration_six.color = "darkgray"
    window.add(decoration_six)

    decoration_seven = GRect(4, 140, x=window.width / 2 - 22, y=630)
    decoration_seven.filled = True
    decoration_seven.fill_color = "black"
    decoration_seven.color = "black"
    window.add(decoration_seven)

    decoration_eight = GRect(25, 70, x=window.width / 2 + 75, y=700)
    decoration_eight.filled = True
    decoration_eight.fill_color = "darkgray"
    decoration_eight.color = "darkgray"
    window.add(decoration_eight)

    decoration_nine = GRect(4, 70, x=window.width / 2 + 75, y=700)
    decoration_nine.filled = True
    decoration_nine.fill_color = "black"
    decoration_nine.color = "black"
    window.add(decoration_nine)

    decoration_ten = GRect(30, 30, x=window.width / 2 - 15, y=210)
    decoration_ten.filled = True
    decoration_ten.fill_color = "dimgray"
    decoration_ten.color = "dimgray"
    window.add(decoration_ten)

    decoration_11 = GRect(10, 60, x=window.width / 2 - 5, y=130)
    decoration_11.filled = True
    decoration_11.fill_color = "gray"
    decoration_11.color = "gray"
    window.add(decoration_11)

    decoration_12 = GRect(60, 2, x=window.width / 2 - 10, y=598)
    decoration_12.filled = True
    decoration_12.fill_color = "darkgray"
    decoration_12.color = "darkgray"
    window.add(decoration_12)

    decoration_13 = GRect(140, 2, x=window.width / 2 - 70, y=628)
    decoration_13.filled = True
    decoration_13.fill_color = "darkgray"
    decoration_13.color = "darkgray"
    window.add(decoration_13)

    decoration_14 = GRect(85, 2, x=window.width / 2 - 10, y=698)
    decoration_14.filled = True
    decoration_14.fill_color = "darkgray"
    decoration_14.color = "darkgray"
    window.add(decoration_14)

    decoration_15 = GRect(84, 2, x=window.width / 2 - 10, y=768)
    decoration_15.filled = True
    decoration_15.fill_color = "darkgray"
    decoration_15.color = "darkgray"
    window.add(decoration_15)

    decoration_16 = GRect(77, 2, x=window.width / 2 - 100, y=768)
    decoration_16.filled = True
    decoration_16.fill_color = "darkgray"
    decoration_16.color = "darkgray"
    window.add(decoration_16)

    decoration_17 = GRect(29, 2, x=window.width / 2 - 50, y=598)
    decoration_17.filled = True
    decoration_17.fill_color = "darkgray"
    decoration_17.color = "darkgray"
    window.add(decoration_17)

    decoration_18 = GRect(52, 2, x=window.width / 2 - 75, y=698)
    decoration_18.filled = True
    decoration_18.fill_color = "darkgray"
    decoration_18.color = "darkgray"
    window.add(decoration_18)

    decoration_19 = GRect(30, 19, x=window.width / 2 - 75, y=770)
    decoration_19.filled = True
    decoration_19.fill_color = "gray"
    decoration_19.color = "gray"
    window.add(decoration_19)

    decoration_20 = GRect(30, 19, x=window.width / 2 + 45, y=770)
    decoration_20.filled = True
    decoration_20.fill_color = "gray"
    decoration_20.color = "gray"
    window.add(decoration_20)

    decoration_21 = GRect(2, 19, x=window.width / 2 - 44, y=770)
    decoration_21.filled = True
    decoration_21.fill_color = "black"
    decoration_21.color = "black"
    window.add(decoration_21)

    decoration_22 = GRect(2, 19, x=window.width / 2 - 41, y=770)
    decoration_22.filled = True
    decoration_22.fill_color = "darkgray"
    decoration_22.color = "darkgray"
    window.add(decoration_22)

    decoration_23 = GRect(2, 19, x=window.width / 2 + 76, y=770)
    decoration_23.filled = True
    decoration_23.fill_color = "black"
    decoration_23.color = "black"
    window.add(decoration_23)

    decoration_24 = GRect(2, 19, x=window.width / 2 + 79, y=770)
    decoration_24.filled = True
    decoration_24.fill_color = "darkgray"
    decoration_24.color = "darkgray"
    window.add(decoration_24)

    decoration_25 = GRect(50, 2, x=window.width / 2 - 10, y=298)
    decoration_25.filled = True
    decoration_25.fill_color = "darkgray"
    decoration_25.color = "darkgray"
    window.add(decoration_25)

    decoration_26 = GRect(17, 2, x=window.width / 2 - 40, y=298)
    decoration_26.filled = True
    decoration_26.fill_color = "darkgray"
    decoration_26.color = "darkgray"
    window.add(decoration_26)

    decoration_27 = GRect(4, 60, x=window.width / 2 - 2, y=130)
    decoration_27.filled = True
    decoration_27.fill_color = "dimgray"
    decoration_27.color = "dimgray"
    window.add(decoration_27)

    decoration_28 = GRect(30, 2, x=window.width / 2 - 15, y=188)
    decoration_28.filled = True
    decoration_28.fill_color = "gray"
    decoration_28.color = "gray"
    window.add(decoration_28)

    decoration_29 = GRect(10, 20, x=window.width / 2 + 5, y=150)
    decoration_29.filled = True
    decoration_29.fill_color = "dimgray"
    decoration_29.color = "black"
    window.add(decoration_29)

    decoration_29 = GRect(10, 20, x=window.width / 2 - 15, y=150)
    decoration_29.filled = True
    decoration_29.fill_color = "lightgray"
    decoration_29.color = "black"
    window.add(decoration_29)

    decoration_30 = GRect(2, 57, x=window.width / 2 - 5, y=130)
    decoration_30.filled = True
    decoration_30.fill_color = "black"
    decoration_30.color = "black"
    window.add(decoration_30)

    decoration_31 = GRect(20, 4, x=window.width / 2 - 10, y=125)
    decoration_31.filled = True
    decoration_31.fill_color = "gray"
    decoration_31.color = "gray"
    window.add(decoration_31)

    decoration_32 = GRect(20, 2, x=window.width / 2 - 10, y=127)
    decoration_32.filled = True
    decoration_32.fill_color = "black"
    decoration_32.color = "black"
    window.add(decoration_32)

    decoration_33 = GRect(20, 2, x=window.width / 2 - 10, y=110)
    decoration_33.filled = True
    decoration_33.fill_color = "white"
    decoration_33.color = "white"
    window.add(decoration_33)

    decoration_34 = GRect(20, 3, x=window.width / 2 - 10, y=112)
    decoration_34.filled = True
    decoration_34.fill_color = "gray"
    decoration_34.color = "gray"
    window.add(decoration_34)

    decoration_35 = GRect(4, 6, x=window.width / 2 - 2, y=103)
    decoration_35.filled = True
    decoration_35.fill_color = "gray"
    decoration_35.color = "gray"
    window.add(decoration_35)

    decoration_36 = GRect(4, 6, x=window.width / 2 - 2, y=95)
    decoration_36.filled = True
    decoration_36.fill_color = "gray"
    decoration_36.color = "gray"
    window.add(decoration_36)

    decoration_37 = GRect(4, 6, x=window.width / 2 - 2, y=87)
    decoration_37.filled = True
    decoration_37.fill_color = "gray"
    decoration_37.color = "gray"
    window.add(decoration_37)

    oval_one = GOval(10, 10, x=window.width / 2 - 26, y=210)
    oval_one.filled = True
    oval_one.fill_color = "gray"
    window.add(oval_one)

    oval_two = GOval(10, 10, x=window.width / 2 + 15, y=210)
    oval_two.filled = True
    oval_two.fill_color = "gray"
    window.add(oval_two)

    oval_three = GOval(10, 10, x=window.width / 2 - 5, y=190)
    oval_three.filled = True
    oval_three.fill_color = "lightgray"
    window.add(oval_three)

    oval_four = GOval(10, 10, x=window.width / 2 - 15, y=190)
    oval_four.filled = True
    oval_four.fill_color = "lightgray"
    window.add(oval_four)

    oval_five = GOval(10, 10, x=window.width / 2 + 5, y=190)
    oval_five.filled = True
    oval_five.fill_color = "lightgray"
    window.add(oval_five)

    rect_one = GRect(10, 20, x=window.width / 2 - 26, y=220)
    rect_one.filled = True
    rect_one.fill_color = "gray"
    window.add(rect_one)

    rect_two = GRect(10, 20, x=window.width / 2 + 15, y=220)
    rect_two.filled = True
    rect_two.fill_color = "gray"
    window.add(rect_two)

    main_body_window_one = GRect(2, 300, x=window.width / 2 - 45, y=300)
    main_body_window_one.filled = True
    main_body_window_one.fill_color = "black"
    main_body_window_one.color = "black"
    window.add(main_body_window_one)

    main_body_window_two = GRect(2, 300, x=window.width / 2 - 39, y=300)
    main_body_window_two.filled = True
    main_body_window_two.fill_color = "black"
    main_body_window_two.color = "black"
    window.add(main_body_window_two)

    main_body_window_three = GRect(2, 300, x=window.width / 2 - 33, y=300)
    main_body_window_three.filled = True
    main_body_window_three.fill_color = "black"
    main_body_window_three.color = "black"
    window.add(main_body_window_three)

    main_body_window_four = GRect(2, 300, x=window.width / 2 - 27, y=300)
    main_body_window_four.filled = True
    main_body_window_four.fill_color = "black"
    main_body_window_four.color = "black"
    window.add(main_body_window_four)

    main_body_window_five = GRect(2, 300, x=window.width / 2 + 45, y=300)
    main_body_window_five.filled = True
    main_body_window_five.fill_color = "black"
    main_body_window_five.color = "black"
    window.add(main_body_window_five)

    main_body_window_six = GRect(2, 300, x=window.width / 2 + 39, y=300)
    main_body_window_six.filled = True
    main_body_window_six.fill_color = "black"
    main_body_window_six.color = "black"
    window.add(main_body_window_six)

    main_body_window_seven = GRect(2, 300, x=window.width / 2 + 33, y=300)
    main_body_window_seven.filled = True
    main_body_window_seven.fill_color = "black"
    main_body_window_seven.color = "black"
    window.add(main_body_window_seven)

    main_body_window_eight = GRect(2, 300, x=window.width / 2 + 27, y=300)
    main_body_window_eight.filled = True
    main_body_window_eight.fill_color = "black"
    main_body_window_eight.color = "black"
    window.add(main_body_window_eight)

    main_body_window_nine = GRect(2, 300, x=window.width / 2 + 20, y=300)
    main_body_window_nine.filled = True
    main_body_window_nine.fill_color = "black"
    main_body_window_nine.color = "black"
    window.add(main_body_window_nine)

    main_body_window_ten = GRect(2, 300, x=window.width / 2 + 14, y=300)
    main_body_window_ten.filled = True
    main_body_window_ten.fill_color = "black"
    main_body_window_ten.color = "black"
    window.add(main_body_window_ten)

    main_body_window_eleven = GRect(2, 300, x=window.width / 2 + 8, y=300)
    main_body_window_eleven.filled = True
    main_body_window_eleven.fill_color = "black"
    main_body_window_eleven.color = "black"
    window.add(main_body_window_eleven)

    main_body_window_twelve = GRect(2, 300, x=window.width / 2 + 2, y=300)
    main_body_window_twelve.filled = True
    main_body_window_twelve.fill_color = "black"
    main_body_window_twelve.color = "black"
    window.add(main_body_window_twelve)

    main_body_window_13 = GRect(2, 300, x=window.width / 2 - 4, y=300)
    main_body_window_13.filled = True
    main_body_window_13.fill_color = "black"
    main_body_window_13.color = "black"
    window.add(main_body_window_13)

    main_body_window_14 = GRect(2, 300, x=window.width / 2 - 10, y=300)
    main_body_window_14.filled = True
    main_body_window_14.fill_color = "black"
    main_body_window_14.color = "black"
    window.add(main_body_window_14)

    main_body_window_cross_one = GRect(25, 2, x=window.width/2-50, y=320)
    main_body_window_cross_one.filled = True
    main_body_window_cross_one.fill_color = "dimgray"
    main_body_window_cross_one.color = "dimgray"
    window.add(main_body_window_cross_one)

    main_body_window_cross_two = GRect(25, 2, x=window.width / 2 - 50, y=340)
    main_body_window_cross_two.filled = True
    main_body_window_cross_two.fill_color = "dimgray"
    main_body_window_cross_two.color = "dimgray"
    window.add(main_body_window_cross_two)

    main_body_window_cross_three = GRect(25, 2, x=window.width / 2 - 50, y=360)
    main_body_window_cross_three.filled = True
    main_body_window_cross_three.fill_color = "dimgray"
    main_body_window_cross_three.color = "dimgray"
    window.add(main_body_window_cross_three)

    main_body_window_cross_four = GRect(25, 2, x=window.width / 2 - 50, y=380)
    main_body_window_cross_four.filled = True
    main_body_window_cross_four.fill_color = "dimgray"
    main_body_window_cross_four.color = "dimgray"
    window.add(main_body_window_cross_four)

    main_body_window_cross_five = GRect(25, 2, x=window.width / 2 - 50, y=400)
    main_body_window_cross_five.filled = True
    main_body_window_cross_five.fill_color = "dimgray"
    main_body_window_cross_five.color = "dimgray"
    window.add(main_body_window_cross_five)

    main_body_window_cross_six = GRect(25, 2, x=window.width / 2 - 50, y=420)
    main_body_window_cross_six.filled = True
    main_body_window_cross_six.fill_color = "dimgray"
    main_body_window_cross_six.color = "dimgray"
    window.add(main_body_window_cross_six)

    main_body_window_cross_seven = GRect(25, 2, x=window.width / 2 - 50, y=440)
    main_body_window_cross_seven.filled = True
    main_body_window_cross_seven.fill_color = "dimgray"
    main_body_window_cross_seven.color = "dimgray"
    window.add(main_body_window_cross_seven)

    main_body_window_cross_eight = GRect(25, 2, x=window.width / 2 - 50, y=460)
    main_body_window_cross_eight.filled = True
    main_body_window_cross_eight.fill_color = "dimgray"
    main_body_window_cross_eight.color = "dimgray"
    window.add(main_body_window_cross_eight)

    main_body_window_cross_nine = GRect(25, 2, x=window.width / 2 - 50, y=480)
    main_body_window_cross_nine.filled = True
    main_body_window_cross_nine.fill_color = "dimgray"
    main_body_window_cross_nine.color = "dimgray"
    window.add(main_body_window_cross_nine)

    main_body_window_cross_ten = GRect(25, 2, x=window.width / 2 - 50, y=500)
    main_body_window_cross_ten.filled = True
    main_body_window_cross_ten.fill_color = "dimgray"
    main_body_window_cross_ten.color = "dimgray"
    window.add(main_body_window_cross_ten)

    main_body_window_cross_11 = GRect(25, 2, x=window.width / 2 - 50, y=520)
    main_body_window_cross_11.filled = True
    main_body_window_cross_11.fill_color = "dimgray"
    main_body_window_cross_11.color = "dimgray"
    window.add(main_body_window_cross_11)

    main_body_window_cross_12 = GRect(25, 2, x=window.width / 2 - 50, y=540)
    main_body_window_cross_12.filled = True
    main_body_window_cross_12.fill_color = "dimgray"
    main_body_window_cross_12.color = "dimgray"
    window.add(main_body_window_cross_12)

    main_body_window_cross_13 = GRect(25, 2, x=window.width / 2 - 50, y=560)
    main_body_window_cross_13.filled = True
    main_body_window_cross_13.fill_color = "dimgray"
    main_body_window_cross_13.color = "dimgray"
    window.add(main_body_window_cross_13)

    main_body_window_cross_14 = GRect(25, 2, x=window.width / 2 - 50, y=580)
    main_body_window_cross_14.filled = True
    main_body_window_cross_14.fill_color = "dimgray"
    main_body_window_cross_14.color = "dimgray"
    window.add(main_body_window_cross_14)

    main_body_window_cross_15 = GRect(30, 2, x=window.width / 2 + 20, y=320)
    main_body_window_cross_15.filled = True
    main_body_window_cross_15.fill_color = "dimgray"
    main_body_window_cross_15.color = "dimgray"
    window.add(main_body_window_cross_15)

    main_body_window_cross_16 = GRect(30, 2, x=window.width / 2 + 20, y=340)
    main_body_window_cross_16.filled = True
    main_body_window_cross_16.fill_color = "dimgray"
    main_body_window_cross_16.color = "dimgray"
    window.add(main_body_window_cross_16)

    main_body_window_cross_17 = GRect(30, 2, x=window.width / 2 + 20, y=360)
    main_body_window_cross_17.filled = True
    main_body_window_cross_17.fill_color = "dimgray"
    main_body_window_cross_17.color = "dimgray"
    window.add(main_body_window_cross_17)

    main_body_window_cross_18 = GRect(30, 2, x=window.width / 2 + 20, y=380)
    main_body_window_cross_18.filled = True
    main_body_window_cross_18.fill_color = "dimgray"
    main_body_window_cross_18.color = "dimgray"
    window.add(main_body_window_cross_18)

    main_body_window_cross_19 = GRect(30, 2, x=window.width / 2 + 20, y=400)
    main_body_window_cross_19.filled = True
    main_body_window_cross_19.fill_color = "dimgray"
    main_body_window_cross_19.color = "dimgray"
    window.add(main_body_window_cross_19)

    main_body_window_cross_20 = GRect(30, 2, x=window.width / 2 + 20, y=420)
    main_body_window_cross_20.filled = True
    main_body_window_cross_20.fill_color = "dimgray"
    main_body_window_cross_20.color = "dimgray"
    window.add(main_body_window_cross_20)

    main_body_window_cross_21 = GRect(30, 2, x=window.width / 2 + 20, y=440)
    main_body_window_cross_21.filled = True
    main_body_window_cross_21.fill_color = "dimgray"
    main_body_window_cross_21.color = "dimgray"
    window.add(main_body_window_cross_21)

    main_body_window_cross_22 = GRect(30, 2, x=window.width / 2 + 20, y=460)
    main_body_window_cross_22.filled = True
    main_body_window_cross_22.fill_color = "dimgray"
    main_body_window_cross_22.color = "dimgray"
    window.add(main_body_window_cross_22)

    main_body_window_cross_23 = GRect(30, 2, x=window.width / 2 + 20, y=480)
    main_body_window_cross_23.filled = True
    main_body_window_cross_23.fill_color = "dimgray"
    main_body_window_cross_23.color = "dimgray"
    window.add(main_body_window_cross_23)

    main_body_window_cross_24 = GRect(30, 2, x=window.width / 2 + 20, y=500)
    main_body_window_cross_24.filled = True
    main_body_window_cross_24.fill_color = "dimgray"
    main_body_window_cross_24.color = "dimgray"
    window.add(main_body_window_cross_24)

    main_body_window_cross_25 = GRect(30, 2, x=window.width / 2 + 20, y=520)
    main_body_window_cross_25.filled = True
    main_body_window_cross_25.fill_color = "dimgray"
    main_body_window_cross_25.color = "dimgray"
    window.add(main_body_window_cross_25)

    main_body_window_cross_26 = GRect(30, 2, x=window.width / 2 + 20, y=540)
    main_body_window_cross_26.filled = True
    main_body_window_cross_26.fill_color = "dimgray"
    main_body_window_cross_26.color = "dimgray"
    window.add(main_body_window_cross_26)

    main_body_window_cross_27 = GRect(30, 2, x=window.width / 2 + 20, y=560)
    main_body_window_cross_27.filled = True
    main_body_window_cross_27.fill_color = "dimgray"
    main_body_window_cross_27.color = "dimgray"
    window.add(main_body_window_cross_27)

    main_body_window_cross_28 = GRect(30, 2, x=window.width / 2 + 20, y=580)
    main_body_window_cross_28.filled = True
    main_body_window_cross_28.fill_color = "dimgray"
    main_body_window_cross_28.color = "dimgray"
    window.add(main_body_window_cross_28)

    main_body_window_cross_29 = GRect(30, 2, x=window.width / 2 - 10, y=320)
    main_body_window_cross_29.filled = True
    main_body_window_cross_29.fill_color = "darkgray"
    main_body_window_cross_29.color = "darkgray"
    window.add(main_body_window_cross_29)

    main_body_window_cross_30 = GRect(30, 2, x=window.width / 2 - 10, y=340)
    main_body_window_cross_30.filled = True
    main_body_window_cross_30.fill_color = "darkgray"
    main_body_window_cross_30.color = "darkgray"
    window.add(main_body_window_cross_30)

    main_body_window_cross_31 = GRect(30, 2, x=window.width / 2 - 10, y=360)
    main_body_window_cross_31.filled = True
    main_body_window_cross_31.fill_color = "darkgray"
    main_body_window_cross_31.color = "darkgray"
    window.add(main_body_window_cross_31)

    main_body_window_cross_32 = GRect(30, 2, x=window.width / 2 - 10, y=380)
    main_body_window_cross_32.filled = True
    main_body_window_cross_32.fill_color = "darkgray"
    main_body_window_cross_32.color = "darkgray"
    window.add(main_body_window_cross_32)

    main_body_window_cross_33 = GRect(30, 2, x=window.width / 2 - 10, y=400)
    main_body_window_cross_33.filled = True
    main_body_window_cross_33.fill_color = "darkgray"
    main_body_window_cross_33.color = "darkgray"
    window.add(main_body_window_cross_33)

    main_body_window_cross_34 = GRect(30, 2, x=window.width / 2 - 10, y=420)
    main_body_window_cross_34.filled = True
    main_body_window_cross_34.fill_color = "darkgray"
    main_body_window_cross_34.color = "darkgray"
    window.add(main_body_window_cross_34)

    main_body_window_cross_35 = GRect(30, 2, x=window.width / 2 - 10, y=440)
    main_body_window_cross_35.filled = True
    main_body_window_cross_35.fill_color = "darkgray"
    main_body_window_cross_35.color = "darkgray"
    window.add(main_body_window_cross_35)

    main_body_window_cross_36 = GRect(30, 2, x=window.width / 2 - 10, y=460)
    main_body_window_cross_36.filled = True
    main_body_window_cross_36.fill_color = "darkgray"
    main_body_window_cross_36.color = "darkgray"
    window.add(main_body_window_cross_36)

    main_body_window_cross_37 = GRect(30, 2, x=window.width / 2 - 10, y=480)
    main_body_window_cross_37.filled = True
    main_body_window_cross_37.fill_color = "darkgray"
    main_body_window_cross_37.color = "darkgray"
    window.add(main_body_window_cross_37)

    main_body_window_cross_38 = GRect(30, 2, x=window.width / 2 - 10, y=500)
    main_body_window_cross_38.filled = True
    main_body_window_cross_38.fill_color = "darkgray"
    main_body_window_cross_38.color = "darkgray"
    window.add(main_body_window_cross_38)

    main_body_window_cross_39 = GRect(30, 2, x=window.width / 2 - 10, y=520)
    main_body_window_cross_39.filled = True
    main_body_window_cross_39.fill_color = "darkgray"
    main_body_window_cross_39.color = "darkgray"
    window.add(main_body_window_cross_39)

    main_body_window_cross_40 = GRect(30, 2, x=window.width / 2 - 10, y=540)
    main_body_window_cross_40.filled = True
    main_body_window_cross_40.fill_color = "darkgray"
    main_body_window_cross_40.color = "darkgray"
    window.add(main_body_window_cross_40)

    main_body_window_cross_41 = GRect(30, 2, x=window.width / 2 - 10, y=560)
    main_body_window_cross_41.filled = True
    main_body_window_cross_41.fill_color = "darkgray"
    main_body_window_cross_41.color = "darkgray"
    window.add(main_body_window_cross_41)

    main_body_window_cross_42 = GRect(30, 2, x=window.width / 2 - 10, y=580)
    main_body_window_cross_42.filled = True
    main_body_window_cross_42.fill_color = "darkgray"
    main_body_window_cross_42.color = "darkgray"
    window.add(main_body_window_cross_42)

    head_two_window_one = GRect(2, 20, x=window.width / 2 - 10, y=215)
    head_two_window_one.filled = True
    head_two_window_one.fill_color = "black"
    head_two_window_one.color = "black"
    window.add(head_two_window_one)

    head_two_window_two = GRect(2, 20, x=window.width / 2 - 4, y=215)
    head_two_window_two.filled = True
    head_two_window_two.fill_color = "black"
    head_two_window_two.color = "black"
    window.add(head_two_window_two)

    head_two_window_three = GRect(2, 20, x=window.width / 2 + 2, y=215)
    head_two_window_three.filled = True
    head_two_window_three.fill_color = "black"
    head_two_window_three.color = "black"
    window.add(head_two_window_three)

    head_two_window_four = GRect(2, 20, x=window.width / 2 + 8, y=215)
    head_two_window_four.filled = True
    head_two_window_four.fill_color = "black"
    head_two_window_four.color = "black"
    window.add(head_two_window_four)

    waist_one_window_one = GRect(2, 20, x=window.width / 2 + 64, y=605)
    waist_one_window_one.filled = True
    waist_one_window_one.fill_color = "black"
    waist_one_window_one.color = "black"
    window.add(waist_one_window_one)

    waist_one_window_two = GRect(2, 20, x=window.width / 2 + 58, y=605)
    waist_one_window_two.filled = True
    waist_one_window_two.fill_color = "black"
    waist_one_window_two.color = "black"
    window.add(waist_one_window_two)

    waist_one_window_three = GRect(2, 20, x=window.width / 2 + 45, y=605)
    waist_one_window_three.filled = True
    waist_one_window_three.fill_color = "black"
    waist_one_window_three.color = "black"
    window.add(waist_one_window_three)

    waist_one_window_four = GRect(2, 20, x=window.width / 2 + 38, y=605)
    waist_one_window_four.filled = True
    waist_one_window_four.fill_color = "black"
    waist_one_window_four.color = "black"
    window.add(waist_one_window_four)

    waist_one_window_five = GRect(2, 20, x=window.width / 2 + 31, y=605)
    waist_one_window_five.filled = True
    waist_one_window_five.fill_color = "black"
    waist_one_window_five.color = "black"
    window.add(waist_one_window_five)

    waist_one_window_six = GRect(2, 20, x=window.width / 2 + 24, y=605)
    waist_one_window_six.filled = True
    waist_one_window_six.fill_color = "black"
    waist_one_window_six.color = "black"
    window.add(waist_one_window_six)

    waist_one_window_seven = GRect(2, 20, x=window.width / 2 + 17, y=605)
    waist_one_window_seven.filled = True
    waist_one_window_seven.fill_color = "black"
    waist_one_window_seven.color = "black"
    window.add(waist_one_window_seven)

    waist_one_window_eight = GRect(2, 20, x=window.width / 2 + 10, y=605)
    waist_one_window_eight.filled = True
    waist_one_window_eight.fill_color = "black"
    waist_one_window_eight.color = "black"
    window.add(waist_one_window_eight)

    waist_one_window_nine = GRect(2, 20, x=window.width / 2 + 3, y=605)
    waist_one_window_nine.filled = True
    waist_one_window_nine.fill_color = "black"
    waist_one_window_nine.color = "black"
    window.add(waist_one_window_nine)

    waist_one_window_ten = GRect(2, 20, x=window.width / 2 - 4, y=605)
    waist_one_window_ten.filled = True
    waist_one_window_ten.fill_color = "black"
    waist_one_window_ten.color = "black"
    window.add(waist_one_window_ten)

    waist_one_window_11 = GRect(2, 20, x=window.width / 2 - 11, y=605)
    waist_one_window_11.filled = True
    waist_one_window_11.fill_color = "black"
    waist_one_window_11.color = "black"
    window.add(waist_one_window_11)

    waist_one_window_12 = GRect(2, 20, x=window.width / 2 - 18, y=605)
    waist_one_window_12.filled = True
    waist_one_window_12.fill_color = "black"
    waist_one_window_12.color = "black"
    window.add(waist_one_window_12)

    waist_one_window_13 = GRect(2, 20, x=window.width / 2 - 25, y=605)
    waist_one_window_13.filled = True
    waist_one_window_13.fill_color = "black"
    waist_one_window_13.color = "black"
    window.add(waist_one_window_13)

    waist_one_window_14 = GRect(2, 20, x=window.width / 2 - 32, y=605)
    waist_one_window_14.filled = True
    waist_one_window_14.fill_color = "black"
    waist_one_window_14.color = "black"
    window.add(waist_one_window_14)

    waist_one_window_15 = GRect(2, 20, x=window.width / 2 - 39, y=605)
    waist_one_window_15.filled = True
    waist_one_window_15.fill_color = "black"
    waist_one_window_15.color = "black"
    window.add(waist_one_window_15)

    waist_one_window_16 = GRect(2, 20, x=window.width / 2 - 46, y=605)
    waist_one_window_16.filled = True
    waist_one_window_16.fill_color = "black"
    waist_one_window_16.color = "black"
    window.add(waist_one_window_16)

    waist_one_window_17 = GRect(2, 20, x=window.width / 2 - 53, y=605)
    waist_one_window_17.filled = True
    waist_one_window_17.fill_color = "black"
    waist_one_window_17.color = "black"
    window.add(waist_one_window_17)

    waist_one_window_18 = GRect(2, 20, x=window.width / 2 - 60, y=605)
    waist_one_window_18.filled = True
    waist_one_window_18.fill_color = "black"
    waist_one_window_18.color = "black"
    window.add(waist_one_window_18)

    waist_one_window_19 = GRect(2, 20, x=window.width / 2 - 67, y=605)
    waist_one_window_19.filled = True
    waist_one_window_19.fill_color = "black"
    waist_one_window_19.color = "black"
    window.add(waist_one_window_19)

    head_one_window_one = GRect(2, 50, x=window.width / 2 + 34, y=245)
    head_one_window_one.filled = True
    head_one_window_one.fill_color = "black"
    head_one_window_one.color = "black"
    window.add(head_one_window_one)

    head_one_window_two = GRect(2, 50, x=window.width / 2 + 27, y=245)
    head_one_window_two.filled = True
    head_one_window_two.fill_color = "black"
    head_one_window_two.color = "black"
    window.add(head_one_window_two)

    head_one_window_three = GRect(2, 50, x=window.width / 2 + 19, y=245)
    head_one_window_three.filled = True
    head_one_window_three.fill_color = "black"
    head_one_window_three.color = "black"
    window.add(head_one_window_three)

    head_one_window_four = GRect(2, 50, x=window.width / 2 + 11, y=245)
    head_one_window_four.filled = True
    head_one_window_four.fill_color = "black"
    head_one_window_four.color = "black"
    window.add(head_one_window_four)

    head_one_window_five = GRect(2, 50, x=window.width / 2 + 3, y=245)
    head_one_window_five.filled = True
    head_one_window_five.fill_color = "black"
    head_one_window_five.color = "black"
    window.add(head_one_window_five)

    head_one_window_six = GRect(2, 50, x=window.width / 2 - 5, y=245)
    head_one_window_six.filled = True
    head_one_window_six.fill_color = "black"
    head_one_window_six.color = "black"
    window.add(head_one_window_six)

    head_one_window_seven = GRect(2, 50, x=window.width / 2 - 13, y=245)
    head_one_window_seven.filled = True
    head_one_window_seven.fill_color = "black"
    head_one_window_seven.color = "black"
    window.add(head_one_window_seven)

    head_one_window_eight = GRect(2, 50, x=window.width / 2 - 29, y=245)
    head_one_window_eight.filled = True
    head_one_window_eight.fill_color = "black"
    head_one_window_eight.color = "black"
    window.add(head_one_window_eight)

    head_one_window_nine = GRect(2, 50, x=window.width / 2 - 36, y=245)
    head_one_window_nine.filled = True
    head_one_window_nine.fill_color = "black"
    head_one_window_nine.color = "black"
    window.add(head_one_window_nine)

    head_one_window_cross_one = GRect(15, 2, x=window.width / 2 - 40, y=260)
    head_one_window_cross_one.filled = True
    head_one_window_cross_one.fill_color = "dimgray"
    head_one_window_cross_one.color = "dimgray"
    window.add(head_one_window_cross_one)

    head_one_window_cross_two = GRect(15, 2, x=window.width / 2 - 40, y=280)
    head_one_window_cross_two.filled = True
    head_one_window_cross_two.fill_color = "dimgray"
    head_one_window_cross_two.color = "dimgray"
    window.add(head_one_window_cross_two)

    head_one_window_cross_three = GRect(20, 2, x=window.width / 2 + 20, y=260)
    head_one_window_cross_three.filled = True
    head_one_window_cross_three.fill_color = "dimgray"
    head_one_window_cross_three.color = "dimgray"
    window.add(head_one_window_cross_three)

    head_one_window_cross_four = GRect(20, 2, x=window.width / 2 + 20, y=280)
    head_one_window_cross_four.filled = True
    head_one_window_cross_four.fill_color = "dimgray"
    head_one_window_cross_four.color = "dimgray"
    window.add(head_one_window_cross_four)

    head_one_window_cross_five = GRect(35, 2, x=window.width / 2 - 15, y=260)
    head_one_window_cross_five.filled = True
    head_one_window_cross_five.fill_color = "darkgray"
    head_one_window_cross_five.color = "darkgray"
    window.add(head_one_window_cross_five)

    head_one_window_cross_six = GRect(35, 2, x=window.width / 2 - 15, y=280)
    head_one_window_cross_six.filled = True
    head_one_window_cross_six.fill_color = "darkgray"
    head_one_window_cross_six.color = "darkgray"
    window.add(head_one_window_cross_six)

    waist_two_window_one = GRect(2, 60, x=window.width / 2 + 68, y=635)
    waist_two_window_one.filled = True
    waist_two_window_one.fill_color = "black"
    waist_two_window_one.color = "black"
    window.add(waist_two_window_one)

    waist_two_window_two = GRect(2, 60, x=window.width / 2 + 61, y=635)
    waist_two_window_two.filled = True
    waist_two_window_two.fill_color = "black"
    waist_two_window_two.color = "black"
    window.add(waist_two_window_two)

    waist_two_window_three = GRect(2, 60, x=window.width / 2 + 54, y=635)
    waist_two_window_three.filled = True
    waist_two_window_three.fill_color = "black"
    waist_two_window_three.color = "black"
    window.add(waist_two_window_three)

    waist_two_window_four = GRect(2, 60, x=window.width / 2 + 47, y=635)
    waist_two_window_four.filled = True
    waist_two_window_four.fill_color = "black"
    waist_two_window_four.color = "black"
    window.add(waist_two_window_four)

    waist_two_window_five = GRect(2, 60, x=window.width / 2 + 40, y=635)
    waist_two_window_five.filled = True
    waist_two_window_five.fill_color = "black"
    waist_two_window_five.color = "black"
    window.add(waist_two_window_five)

    waist_two_window_six = GRect(2, 60, x=window.width / 2 + 33, y=635)
    waist_two_window_six.filled = True
    waist_two_window_six.fill_color = "black"
    waist_two_window_six.color = "black"
    window.add(waist_two_window_six)

    waist_two_window_seven = GRect(2, 60, x=window.width / 2 + 26, y=635)
    waist_two_window_seven.filled = True
    waist_two_window_seven.fill_color = "black"
    waist_two_window_seven.color = "black"
    window.add(waist_two_window_seven)

    waist_two_window_eight = GRect(2, 60, x=window.width / 2 + 14, y=635)
    waist_two_window_eight.filled = True
    waist_two_window_eight.fill_color = "black"
    waist_two_window_eight.color = "black"
    window.add(waist_two_window_eight)

    waist_two_window_nine = GRect(2, 60, x=window.width / 2 + 7, y=635)
    waist_two_window_nine.filled = True
    waist_two_window_nine.fill_color = "black"
    waist_two_window_nine.color = "black"
    window.add(waist_two_window_nine)

    waist_two_window_ten = GRect(2, 60, x=window.width / 2, y=635)
    waist_two_window_ten.filled = True
    waist_two_window_ten.fill_color = "black"
    waist_two_window_ten.color = "black"
    window.add(waist_two_window_ten)

    waist_two_window_11 = GRect(2, 60, x=window.width / 2 - 7, y=635)
    waist_two_window_11.filled = True
    waist_two_window_11.fill_color = "black"
    waist_two_window_11.color = "black"
    window.add(waist_two_window_11)

    waist_two_window_12 = GRect(2, 60, x=window.width / 2 - 14, y=635)
    waist_two_window_12.filled = True
    waist_two_window_12.fill_color = "black"
    waist_two_window_12.color = "black"
    window.add(waist_two_window_12)

    waist_two_window_13 = GRect(2, 60, x=window.width / 2 - 29, y=635)
    waist_two_window_13.filled = True
    waist_two_window_13.fill_color = "black"
    waist_two_window_13.color = "black"
    window.add(waist_two_window_13)

    waist_two_window_14 = GRect(2, 60, x=window.width / 2 - 36, y=635)
    waist_two_window_14.filled = True
    waist_two_window_14.fill_color = "black"
    waist_two_window_14.color = "black"
    window.add(waist_two_window_14)

    waist_two_window_15 = GRect(2, 60, x=window.width / 2 - 43, y=635)
    waist_two_window_15.filled = True
    waist_two_window_15.fill_color = "black"
    waist_two_window_15.color = "black"
    window.add(waist_two_window_15)

    waist_two_window_16 = GRect(2, 60, x=window.width / 2 - 50, y=635)
    waist_two_window_16.filled = True
    waist_two_window_16.fill_color = "black"
    waist_two_window_16.color = "black"
    window.add(waist_two_window_16)

    waist_two_window_17 = GRect(2, 60, x=window.width / 2 - 57, y=635)
    waist_two_window_17.filled = True
    waist_two_window_17.fill_color = "black"
    waist_two_window_17.color = "black"
    window.add(waist_two_window_17)

    waist_two_window_18 = GRect(2, 60, x=window.width / 2 - 64, y=635)
    waist_two_window_18.filled = True
    waist_two_window_18.fill_color = "black"
    waist_two_window_18.color = "black"
    window.add(waist_two_window_18)

    waist_two_window_19 = GRect(2, 60, x=window.width / 2 - 71, y=635)
    waist_two_window_19.filled = True
    waist_two_window_19.fill_color = "black"
    waist_two_window_19.color = "black"
    window.add(waist_two_window_19)

    waist_two_window_cross_one = GRect(45, 2, x=window.width / 2 - 71, y=655)
    waist_two_window_cross_one.filled = True
    waist_two_window_cross_one.fill_color = "dimgray"
    waist_two_window_cross_one.color = "dimgray"
    window.add(waist_two_window_cross_one)

    waist_two_window_cross_two = GRect(45, 2, x=window.width / 2 - 71, y=675)
    waist_two_window_cross_two.filled = True
    waist_two_window_cross_two.fill_color = "dimgray"
    waist_two_window_cross_two.color = "dimgray"
    window.add(waist_two_window_cross_two)

    waist_two_window_cross_three = GRect(30, 2, x=window.width / 2 - 14, y=655)
    waist_two_window_cross_three.filled = True
    waist_two_window_cross_three.fill_color = "darkgray"
    waist_two_window_cross_three.color = "darkgray"
    window.add(waist_two_window_cross_three)

    waist_two_window_cross_four = GRect(30, 2, x=window.width / 2 - 14, y=675)
    waist_two_window_cross_four.filled = True
    waist_two_window_cross_four.fill_color = "darkgray"
    waist_two_window_cross_four.color = "darkgray"
    window.add(waist_two_window_cross_four)

    waist_two_window_cross_five = GRect(45, 2, x=window.width / 2 + 26, y=655)
    waist_two_window_cross_five.filled = True
    waist_two_window_cross_five.fill_color = "dimgray"
    waist_two_window_cross_five.color = "dimgray"
    window.add(waist_two_window_cross_five)

    waist_two_window_cross_six = GRect(45, 2, x=window.width / 2 + 26, y=675)
    waist_two_window_cross_six.filled = True
    waist_two_window_cross_six.fill_color = "dimgray"
    waist_two_window_cross_six.color = "dimgray"
    window.add(waist_two_window_cross_six)

    base_one_window_one = GRect(2, 60, x=window.width / 2 + 92, y=705)
    base_one_window_one.filled = True
    base_one_window_one.fill_color = "black"
    base_one_window_one.color = "black"
    window.add(base_one_window_one)

    base_one_window_two = GRect(2, 60, x=window.width / 2 + 84, y=705)
    base_one_window_two.filled = True
    base_one_window_two.fill_color = "black"
    base_one_window_two.color = "black"
    window.add(base_one_window_two)

    base_one_window_three = GRect(2, 60, x=window.width / 2 + 68, y=705)
    base_one_window_three.filled = True
    base_one_window_three.fill_color = "black"
    base_one_window_three.color = "black"
    window.add(base_one_window_three)

    base_one_window_four = GRect(2, 60, x=window.width / 2 + 61, y=705)
    base_one_window_four.filled = True
    base_one_window_four.fill_color = "black"
    base_one_window_four.color = "black"
    window.add(base_one_window_four)

    base_one_window_five = GRect(2, 60, x=window.width / 2 + 54, y=705)
    base_one_window_five.filled = True
    base_one_window_five.fill_color = "black"
    base_one_window_five.color = "black"
    window.add(base_one_window_five)

    base_one_window_six = GRect(2, 60, x=window.width / 2 + 47, y=705)
    base_one_window_six.filled = True
    base_one_window_six.fill_color = "black"
    base_one_window_six.color = "black"
    window.add(base_one_window_six)

    base_one_window_seven = GRect(2, 60, x=window.width / 2 + 40, y=705)
    base_one_window_seven.filled = True
    base_one_window_seven.fill_color = "black"
    base_one_window_seven.color = "black"
    window.add(base_one_window_seven)

    base_one_window_eight = GRect(2, 60, x=window.width / 2 + 33, y=705)
    base_one_window_eight.filled = True
    base_one_window_eight.fill_color = "black"
    base_one_window_eight.color = "black"
    window.add(base_one_window_eight)

    base_one_window_nine = GRect(2, 60, x=window.width / 2 + 26, y=705)
    base_one_window_nine.filled = True
    base_one_window_nine.fill_color = "black"
    base_one_window_nine.color = "black"
    window.add(base_one_window_nine)

    base_one_window_ten = GRect(2, 60, x=window.width / 2 + 14, y=705)
    base_one_window_ten.filled = True
    base_one_window_ten.fill_color = "black"
    base_one_window_ten.color = "black"
    window.add(base_one_window_ten)

    base_one_window_11= GRect(2, 60, x=window.width / 2 + 7, y=705)
    base_one_window_11.filled = True
    base_one_window_11.fill_color = "black"
    base_one_window_11.color = "black"
    window.add(base_one_window_11)

    base_one_window_12 = GRect(2, 60, x=window.width / 2, y=705)
    base_one_window_12.filled = True
    base_one_window_12.fill_color = "black"
    base_one_window_12.color = "black"
    window.add(base_one_window_12)

    base_one_window_13 = GRect(2, 60, x=window.width / 2 - 7, y=705)
    base_one_window_13.filled = True
    base_one_window_13.fill_color = "black"
    base_one_window_13.color = "black"
    window.add(base_one_window_13)

    base_one_window_14 = GRect(2, 60, x=window.width / 2 - 14, y=705)
    base_one_window_14.filled = True
    base_one_window_14.fill_color = "black"
    base_one_window_14.color = "black"
    window.add(base_one_window_14)

    base_one_window_15 = GRect(2, 60, x=window.width / 2 - 29, y=705)
    base_one_window_15.filled = True
    base_one_window_15.fill_color = "black"
    base_one_window_15.color = "black"
    window.add(base_one_window_15)

    base_one_window_16 = GRect(2, 60, x=window.width / 2 - 36, y=705)
    base_one_window_16.filled = True
    base_one_window_16.fill_color = "black"
    base_one_window_16.color = "black"
    window.add(base_one_window_16)

    base_one_window_17 = GRect(2, 60, x=window.width / 2 - 43, y=705)
    base_one_window_17.filled = True
    base_one_window_17.fill_color = "black"
    base_one_window_17.color = "black"
    window.add(base_one_window_17)

    base_one_window_18 = GRect(2, 60, x=window.width / 2 - 50, y=705)
    base_one_window_18.filled = True
    base_one_window_18.fill_color = "black"
    base_one_window_18.color = "black"
    window.add(base_one_window_18)

    base_one_window_19 = GRect(2, 60, x=window.width / 2 - 57, y=705)
    base_one_window_19.filled = True
    base_one_window_19.fill_color = "black"
    base_one_window_19.color = "black"
    window.add(base_one_window_19)

    base_one_window_20 = GRect(2, 60, x=window.width / 2 - 64, y=705)
    base_one_window_20.filled = True
    base_one_window_20.fill_color = "black"
    base_one_window_20.color = "black"
    window.add(base_one_window_20)

    base_one_window_21 = GRect(2, 60, x=window.width / 2 - 71, y=705)
    base_one_window_21.filled = True
    base_one_window_21.fill_color = "black"
    base_one_window_21.color = "black"
    window.add(base_one_window_21)

    base_one_window_22 = GRect(2, 60, x=window.width / 2 - 78, y=705)
    base_one_window_22.filled = True
    base_one_window_22.fill_color = "black"
    base_one_window_22.color = "black"
    window.add(base_one_window_22)

    base_one_window_23 = GRect(2, 60, x=window.width / 2 - 85, y=705)
    base_one_window_23.filled = True
    base_one_window_23.fill_color = "black"
    base_one_window_23.color = "black"
    window.add(base_one_window_23)

    base_one_window_24 = GRect(2, 60, x=window.width / 2 - 92, y=705)
    base_one_window_24.filled = True
    base_one_window_24.fill_color = "black"
    base_one_window_24.color = "black"
    window.add(base_one_window_24)

    base_one_window_cross_one = GRect(65, 2, x=window.width / 2 - 92, y=725)
    base_one_window_cross_one.filled = True
    base_one_window_cross_one.fill_color = "dimgray"
    base_one_window_cross_one.color = "dimgray"
    window.add(base_one_window_cross_one)

    base_one_window_cross_two = GRect(65, 2, x=window.width / 2 - 92, y=745)
    base_one_window_cross_two.filled = True
    base_one_window_cross_two.fill_color = "dimgray"
    base_one_window_cross_two.color = "dimgray"
    window.add(base_one_window_cross_two)

    base_one_window_cross_three = GRect(45, 2, x=window.width / 2 + 26, y=725)
    base_one_window_cross_three.filled = True
    base_one_window_cross_three.fill_color = "dimgray"
    base_one_window_cross_three.color = "dimgray"
    window.add(base_one_window_cross_three)

    base_one_window_cross_four = GRect(45, 2, x=window.width / 2 + 26, y=745)
    base_one_window_cross_four.filled = True
    base_one_window_cross_four.fill_color = "dimgray"
    base_one_window_cross_four.color = "dimgray"
    window.add(base_one_window_cross_four)

    base_one_window_cross_five = GRect(35, 2, x=window.width / 2 - 15, y=725)
    base_one_window_cross_five.filled = True
    base_one_window_cross_five.fill_color = "darkgray"
    base_one_window_cross_five.color = "darkgray"
    window.add(base_one_window_cross_five)

    base_one_window_cross_six = GRect(35, 2, x=window.width / 2 - 15, y=745)
    base_one_window_cross_six.filled = True
    base_one_window_cross_six.fill_color = "darkgray"
    base_one_window_cross_six.color = "darkgray"
    window.add(base_one_window_cross_six)

    base_one_window_cross_seven = GRect(20, 2, x=window.width / 2 + 80, y=725)
    base_one_window_cross_seven.filled = True
    base_one_window_cross_seven.fill_color = "darkgray"
    base_one_window_cross_seven.color = "darkgray"
    window.add(base_one_window_cross_seven)

    base_one_window_cross_eight = GRect(20, 2, x=window.width / 2 + 80, y=745)
    base_one_window_cross_eight.filled = True
    base_one_window_cross_eight.fill_color = "darkgray"
    base_one_window_cross_eight.color = "darkgray"
    window.add(base_one_window_cross_eight)

    base_two_window_one = GRect(65, 2, x=window.width / 2 - 145, y=775)
    base_two_window_one.filled = True
    base_two_window_one.fill_color = "black"
    base_two_window_one.color = "black"
    window.add(base_two_window_one)

    base_two_window_two = GRect(20, 2, x=window.width / 2 - 70, y=775)
    base_two_window_two.filled = True
    base_two_window_two.fill_color = "black"
    base_two_window_two.color = "black"
    window.add(base_two_window_two)

    base_two_window_three = GRect(75, 2, x=window.width / 2 - 35, y=775)
    base_two_window_three.filled = True
    base_two_window_three.fill_color = "black"
    base_two_window_three.color = "black"
    window.add(base_two_window_three)

    base_two_window_four = GRect(20, 2, x=window.width / 2 + 50, y=775)
    base_two_window_four.filled = True
    base_two_window_four.fill_color = "black"
    base_two_window_four.color = "black"
    window.add(base_two_window_four)

    base_two_window_five = GRect(60, 2, x=window.width / 2 + 85, y=775)
    base_two_window_five.filled = True
    base_two_window_five.fill_color = "black"
    base_two_window_five.color = "black"
    window.add(base_two_window_five)

    base_two_window_six = GRect(2, 10, x=window.width / 2 - 145, y=780)
    base_two_window_six.filled = True
    base_two_window_six.fill_color = "black"
    base_two_window_six.color = "black"
    window.add(base_two_window_six)

    base_two_window_seven = GRect(2, 10, x=window.width / 2 - 138, y=780)
    base_two_window_seven.filled = True
    base_two_window_seven.fill_color = "black"
    base_two_window_seven.color = "black"
    window.add(base_two_window_seven)

    base_two_window_eight = GRect(2, 10, x=window.width / 2 - 131, y=780)
    base_two_window_eight.filled = True
    base_two_window_eight.fill_color = "black"
    base_two_window_eight.color = "black"
    window.add(base_two_window_eight)

    base_two_window_nine = GRect(2, 10, x=window.width / 2 - 124, y=780)
    base_two_window_nine.filled = True
    base_two_window_nine.fill_color = "black"
    base_two_window_nine.color = "black"
    window.add(base_two_window_nine)

    base_two_window_ten = GRect(2, 10, x=window.width / 2 - 117, y=780)
    base_two_window_ten.filled = True
    base_two_window_ten.fill_color = "black"
    base_two_window_ten.color = "black"
    window.add(base_two_window_ten)

    base_two_window_11 = GRect(2, 10, x=window.width / 2 - 110, y=780)
    base_two_window_11.filled = True
    base_two_window_11.fill_color = "black"
    base_two_window_11.color = "black"
    window.add(base_two_window_11)

    base_two_window_12 = GRect(2, 10, x=window.width / 2 - 103, y=780)
    base_two_window_12.filled = True
    base_two_window_12.fill_color = "black"
    base_two_window_12.color = "black"
    window.add(base_two_window_12)

    base_two_window_13 = GRect(2, 10, x=window.width / 2 - 96, y=780)
    base_two_window_13.filled = True
    base_two_window_13.fill_color = "black"
    base_two_window_13.color = "black"
    window.add(base_two_window_13)

    base_two_window_14 = GRect(2, 10, x=window.width / 2 - 89, y=780)
    base_two_window_14.filled = True
    base_two_window_14.fill_color = "black"
    base_two_window_14.color = "black"
    window.add(base_two_window_14)

    base_two_window_15 = GRect(2, 10, x=window.width / 2 - 82, y=780)
    base_two_window_15.filled = True
    base_two_window_15.fill_color = "black"
    base_two_window_15.color = "black"
    window.add(base_two_window_15)

    base_two_window_16 = GRect(2, 10, x=window.width / 2 - 70, y=780)
    base_two_window_16.filled = True
    base_two_window_16.fill_color = "black"
    base_two_window_16.color = "black"
    window.add(base_two_window_16)

    base_two_window_17 = GRect(2, 10, x=window.width / 2 - 64, y=780)
    base_two_window_17.filled = True
    base_two_window_17.fill_color = "black"
    base_two_window_17.color = "black"
    window.add(base_two_window_17)

    base_two_window_18 = GRect(2, 10, x=window.width / 2 - 58, y=780)
    base_two_window_18.filled = True
    base_two_window_18.fill_color = "black"
    base_two_window_18.color = "black"
    window.add(base_two_window_18)

    base_two_window_19 = GRect(2, 10, x=window.width / 2 - 52, y=780)
    base_two_window_19.filled = True
    base_two_window_19.fill_color = "black"
    base_two_window_19.color = "black"
    window.add(base_two_window_19)

    base_two_window_20 = GRect(2, 10, x=window.width / 2 - 34, y=780)
    base_two_window_20.filled = True
    base_two_window_20.fill_color = "black"
    base_two_window_20.color = "black"
    window.add(base_two_window_20)

    base_two_window_21 = GRect(2, 10, x=window.width / 2 - 26, y=780)
    base_two_window_21.filled = True
    base_two_window_21.fill_color = "black"
    base_two_window_21.color = "black"
    window.add(base_two_window_21)

    base_two_window_22 = GRect(2, 10, x=window.width / 2 - 18, y=780)
    base_two_window_22.filled = True
    base_two_window_22.fill_color = "black"
    base_two_window_22.color = "black"
    window.add(base_two_window_22)

    base_two_window_23 = GRect(2, 10, x=window.width / 2 - 10, y=780)
    base_two_window_23.filled = True
    base_two_window_23.fill_color = "black"
    base_two_window_23.color = "black"
    window.add(base_two_window_23)

    base_two_window_24 = GRect(2, 10, x=window.width / 2 - 2, y=780)
    base_two_window_24.filled = True
    base_two_window_24.fill_color = "black"
    base_two_window_24.color = "black"
    window.add(base_two_window_24)

    base_two_window_25 = GRect(2, 10, x=window.width / 2 + 6, y=780)
    base_two_window_25.filled = True
    base_two_window_25.fill_color = "black"
    base_two_window_25.color = "black"
    window.add(base_two_window_25)

    base_two_window_26 = GRect(2, 10, x=window.width / 2 + 14, y=780)
    base_two_window_26.filled = True
    base_two_window_26.fill_color = "black"
    base_two_window_26.color = "black"
    window.add(base_two_window_26)

    base_two_window_27 = GRect(2, 10, x=window.width / 2 + 22, y=780)
    base_two_window_27.filled = True
    base_two_window_27.fill_color = "black"
    base_two_window_27.color = "black"
    window.add(base_two_window_27)

    base_two_window_28 = GRect(2, 10, x=window.width / 2 + 30, y=780)
    base_two_window_28.filled = True
    base_two_window_28.fill_color = "black"
    base_two_window_28.color = "black"
    window.add(base_two_window_28)

    base_two_window_29 = GRect(2, 10, x=window.width / 2 + 38, y=780)
    base_two_window_29.filled = True
    base_two_window_29.fill_color = "black"
    base_two_window_29.color = "black"
    window.add(base_two_window_29)

    base_two_window_30 = GRect(2, 10, x=window.width / 2 + 50, y=780)
    base_two_window_30.filled = True
    base_two_window_30.fill_color = "black"
    base_two_window_30.color = "black"
    window.add(base_two_window_30)

    base_two_window_31 = GRect(2, 10, x=window.width / 2 + 56, y=780)
    base_two_window_31.filled = True
    base_two_window_31.fill_color = "black"
    base_two_window_31.color = "black"
    window.add(base_two_window_31)

    base_two_window_32 = GRect(2, 10, x=window.width / 2 + 62, y=780)
    base_two_window_32.filled = True
    base_two_window_32.fill_color = "black"
    base_two_window_32.color = "black"
    window.add(base_two_window_32)

    base_two_window_33 = GRect(2, 10, x=window.width / 2 + 68, y=780)
    base_two_window_33.filled = True
    base_two_window_33.fill_color = "black"
    base_two_window_33.color = "black"
    window.add(base_two_window_33)

    base_two_window_34 = GRect(2, 10, x=window.width / 2 + 86, y=780)
    base_two_window_34.filled = True
    base_two_window_34.fill_color = "black"
    base_two_window_34.color = "black"
    window.add(base_two_window_34)

    base_two_window_35 = GRect(2, 10, x=window.width / 2 + 94, y=780)
    base_two_window_35.filled = True
    base_two_window_35.fill_color = "black"
    base_two_window_35.color = "black"
    window.add(base_two_window_35)

    base_two_window_36 = GRect(2, 10, x=window.width / 2 + 102, y=780)
    base_two_window_36.filled = True
    base_two_window_36.fill_color = "black"
    base_two_window_36.color = "black"
    window.add(base_two_window_36)

    base_two_window_37 = GRect(2, 10, x=window.width / 2 + 110, y=780)
    base_two_window_37.filled = True
    base_two_window_37.fill_color = "black"
    base_two_window_37.color = "black"
    window.add(base_two_window_37)

    base_two_window_38 = GRect(2, 10, x=window.width / 2 + 118, y=780)
    base_two_window_38.filled = True
    base_two_window_38.fill_color = "black"
    base_two_window_38.color = "black"
    window.add(base_two_window_38)

    base_two_window_39 = GRect(2, 10, x=window.width / 2 + 126, y=780)
    base_two_window_39.filled = True
    base_two_window_39.fill_color = "black"
    base_two_window_39.color = "black"
    window.add(base_two_window_39)

    base_two_window_40 = GRect(2, 10, x=window.width / 2 + 134, y=780)
    base_two_window_40.filled = True
    base_two_window_40.fill_color = "black"
    base_two_window_40.color = "black"
    window.add(base_two_window_40)

    base_two_window_41 = GRect(2, 10, x=window.width / 2 + 142, y=780)
    base_two_window_41.filled = True
    base_two_window_41.fill_color = "black"
    base_two_window_41.color = "black"
    window.add(base_two_window_41)

    label = GLabel("Empire State Building", x=30, y=40)
    label.font = "-20"
    label.color = "white"
    window.add(label)

    name = GLabel("by Vivian Lin", x=700, y=790)
    name.font = "-15"
    name.color = "white"
    window.add(name)

if __name__ == '__main__':
    main()
