# -*- coding: UTF-8 -*-
#-------------------------------------------------------------------------------
# Name:        exercise_template_tests.py
#
# Purpose:     Test functions for functions in exercise_template.py
#
# Author:      David Viljoen
#
# Created:     24/11/2017
#-------------------------------------------------------------------------------

import sys
import inspect
import Geometry

# Add import statement for the module under test as follows:
# import module_under_test as alias

# For example:
# import world_pop_explorer as wpe
# reload(wpe)

def main():
    # Find and call all functions that begin with "test"
    test_funcs = get_test_functions()
    for test_func in test_funcs:
        test_func()

# Copy/paste/change the test template below to create new test functions, where:
#    - the test function name must begin with the word "test"
#    - desc = Description of the test being made
#    - expected = Expected result from calling the function
#    - actual = Actual result from calling the function
#    - func = Function being tested (the actual function, not the name)"""
#
def template_for_test_functions():
    expected = ""
    actual = ""
    print_test_results(func, expected, actual)

# ------------------------------------------------------------------------------

# Create test functions here using the template_for_test_functions above.
# The name of the test functions needs to begin with "test"

def test_point():
    point1 = Geometry.Point()
    point1.x = 1.0
    point1.y = 2.0
    expected = 3.0
    actual = point1.x+point1.y
    print_test_results(test_point, expected, actual)

def test_line():
    point1 = Geometry.Point()
    point1.x = 1.0
    point1.y = 2.0
    point2 = Geometry.Point()
    point2.x = 4.0
    point2.y = 6.0

    line1 = Geometry.Line()
    line1.from_point = point1
    line1.to_point = point2
    expected = 5.0
    actual = line1.length
    print_test_results(test_line, expected, actual)

def test_polyline():
    point1 = Geometry.Point()
    point1.x = 1.0
    point1.y = 2.0
    point2 = Geometry.Point()
    point2.x = 4.0
    point2.y = 6.0
    line1 = Geometry.Line()
    line1.from_point = point1
    line1.to_point = point2

    point3 = Geometry.Point()
    point3.x = 3.0
    point3.y = 4.0
    point4 = Geometry.Point()
    point4.x = 5.0
    point4.y = 6.0
    line2 = Geometry.Line()
    line2.from_point = point3
    line2.to_point = point4
    polyline1 = Geometry.Polyline(line1,line1.length)
    polyline1.add_segment(line2)
    expected = ((4.0-1.0)**2+(6.0-2.0)**2)**0.5 +((5.0-3.0)**2+(6.0-4.0)**2)**0.5
    actual = polyline1.length
    print_test_results(test_polyline, expected, actual)



# ------------------------------------------------------------------------------
# Test template helper functions.  Code in this section should not need to
# modified.
#
def get_test_functions():
    """Returns a list of functions that begin with the word test in the order
       they appear in this file."""

    test_funcs = [obj for name,obj in inspect.getmembers(sys.modules[__name__])
                     if (inspect.isfunction(obj) and name.startswith('test'))]
    src = inspect.getsource(sys.modules[__name__])
    lines = src.split('\n')

    # Create a dictionary with key=function name and value is 0-based order
    # in the module
    ordered_func_names = dict()
    ordered_funcs = list()
    func_index = 0
    for line in lines:
        if line.find("def test") == 0:
            func_name = line.split("(")[0].split()[1]
            ordered_func_names[func_name] = func_index
            # Create an empty list with sampe number of elements as test
            # functions
            ordered_funcs.append('')
            func_index += 1
    for test_func in test_funcs:
        index = ordered_func_names[test_func.__name__]
        ordered_funcs[index] = test_func
    return ordered_funcs

def print_test_results(func_tested, expected, actual):
    """func_tested is the function being tested
       desc = Test description
       expected = Expected result of test
       actual = Actual result of test """

    if not callable(func_tested):
        raise Exception("{} is not a function".format(func_tested))

    func_name = func_tested.__name__
    desc = func_tested.__doc__
    if expected == actual:
        print "PASSED: {}".format(func_name)
        print "Detail: {}".format(desc)
    else:
        print "FAILED: {}".format(func_name)
        print "Desc:   {}".format(desc)
        print "Expect: {}".format(expected)
        print "Actual: {}".format(actual)
    print ""

if __name__ == '__main__':
    main()
