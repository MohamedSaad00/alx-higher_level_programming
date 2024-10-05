#!/usr/bin/python3
"""Module containing a function that adds two integers.

This module provides the `add_integer` function which takes two numbers
as arguments and returns their sum as an integer. The second argument 
defaults to 98 if not provided."""

def add_integer(a, b=98):
    """ Arguments:
        @a: first integer
        @b: second integer, defaults to 98 if not give."""

    if type(a) not in [int, float]:
        raise TypeError("a must be an integer")
    if type(b) not in [int, float]:
        raise TypeError("b must be an integer")
    return int(a) + int(b)
