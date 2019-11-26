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

class Circle(object):
    @property
    #define radius property
    def radius(self):
        return self.__radius

    @radius.setter
    #set radius property
    def radius(self, radius):
        self.__radius = radius

    @property
    #define area property
    #area depends on radius
    def area(self):
        return math.pi * (self.radius**2)

class Square(object):
    @property
    #define side length property
    def length_of_side(self):
        return self.__length_of_side

    @length_of_side.setter
    #set side property
    def length_of_side(self, length_of_side):
        self.__length_of_side = length_of_side

    @property
    #define area property
    #area depends on radius
    def area(self):
        return (self.length_of_side ** 2)



class Rectangle(object):
    @property
    #define width
    def width(self):
        return self.__width

    @width.setter
    #set width property
    def width (self, width):
        self.__width = width

    @property
    #define height
    def height(self):
        return self.__height

    @height.setter
    #set height property
    def height (self, height):
        self.__height = height

    @property
    #define area property
    #area depends on width and height
    def area(self):
        return (self.width) * (self.height)
