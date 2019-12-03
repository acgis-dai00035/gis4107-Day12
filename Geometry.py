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

def main():
    pass

class Point(object):
    @property
    def x(self):
        return self.__x

    @x.setter
    def x(self,x):
        if type(x)== float:
            self.__x = x
        else:
            raise TypeError, "x must be float"

    @property
    def y(self):
        return self.__y

    @y.setter
    def y(self,y):
        if type(y)== float:
            self.__y = y
        else:
            raise TypeError, "y must be float"

class Line(object):
    @property
    def from_point(self):
        return self.__from_point
    @from_point.setter
    def from_point(self,from_point):
        self.__from_point = from_point
    @property
    def to_point(self):
        return self.__to_point
    @to_point.setter
    def to_point(self,to_point):
        self.__to_point = to_point

    @property
    def length(self):
        return ((self.to_point.x-self.from_point.x)**2+(self.to_point.y-self.from_point.y)**2)**0.5


class Polyline:
    def __init__(self,segments,length):
        self.__segments = segments
        self.__length = length


    @property
    def segments(self):
        return self.__segments


    @property
    def length(self):
        return self.__length

    def add_segment(self,seg):
        self.segments.append(seg)





def func(params):
    """Function documentation:
       - What does function do?
       - What is/are expected parameter value(s)?
       - What does function return, if anything
       - Example usage"""

    pass

if __name__ == '__main__':
    main()