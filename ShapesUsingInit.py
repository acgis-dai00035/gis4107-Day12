# -*- coding: UTF-8 -*-
# ------------------------------------------------------------------------------
# Name:        exercise_template.py
#
# Purpose:     Brief desciption of what module does
#
# Usage:       Module name and required/optional command-line parameters (if any)
#
# Author:      Your name(s)
#
# Created:     dd/mm/yyyy
# ------------------------------------------------------------------------------
import math

class Circle:
    def __init__(self, radius):
        self.__radius = radius


    #define area property
    #area depends on radius
    def area(self):
        return math.pi * (self.__radius**2)




class Square:
    def __init__(self, side):
        self.__side = side



    #define area property
    #area depends on side
    def area(self):
        return self.__side**2



class Rectangle:
    def __init__(self, width, height):
        self.__width = width
        self.__height = height

    #define area property
    #area depends on width and height
    def area(self):
        return (self.__width) * (self.__height)
