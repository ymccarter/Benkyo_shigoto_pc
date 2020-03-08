"""Answers for Homework 1 for CSE-41273"""


# Problem 1
def silly_case(in_string):
    """Given a string, convert it to a string such that each word starts with
        a lower case letter, and the remaining letters are upper case.
        Return the silly case string."""
    return in_string.title().swapcase()


# Problem 2
def dash_stringify(word_list):
    """Given a list of word strings, return a single string with all the
        strings together, with ' - ' in between the words."""
    return ' - '.join(word_list)


# Problem 3
def is_perfect_square(number):
    """Given a number, return True if it is a perfect square,
        else return False"""
    root = number ** 0.5
    # Using the method is_integer() is preferred over trying to compare
    # floats with integers. Methods of float handle issues
    # relating to the slight "slop" sometimes caused by inaccuracies of
    # the internal floating point representation.
    return root.is_integer()


# Problem 3
# If you want to check the input is correct.
# Some students asked how to do this even though it is not needed.
# We will be talking about exceptions and dealing with them in week 3.
def is_perfect_square2(number):
    """Given a number, return True if it is a perfect square,
        else return False"""
    if not isinstance(number, int):
        raise ValueError("Number must be an integer")
    if number < 0:
        raise ValueError("Number cannot be negative")
    root = number ** 0.5
    return root.is_integer()


# Problem 4
# Using Wikipedia's pseudocode and "truthiness" of modulo results
def is_leap_year(year):
    """Given a year, return True if it is a leap year, else return False"""
    # if (year is not divisible by 4) then (it is a common year)
    if year % 4:
        return False
    # else if (year is not divisible by 100) then (it is a leap year)
    if year % 100:
        return True
    # else if (year is not divisible by 400) then (it is a common year)
    if year % 400:
        return False
    # else (it is a leap year)
    return True


# Or if you prefer to do it in one line:
def is_leap_year2(year):
    """Given a year, return True if it is a leap year, else return False"""
    return year % 4 == 0 and (year % 100 != 0 or year % 400 == 0)
