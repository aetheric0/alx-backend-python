#!/usr/bin/env python3
""" Implements a type-annotated function make_multiplier
that takes a float multiplier as argument and returns a
function that multiplies a float by multiplier.
"""
from typing import Callable


def make_multiplier(multiplier: float) -> Callable[[float], float]:
    """ Returns a function that multiplies 'multiplier' by a float
    """
    def my_multiplier(value: float):
        return value * multiplier
    return my_multiplier
