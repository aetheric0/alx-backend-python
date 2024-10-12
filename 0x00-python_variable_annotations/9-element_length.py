#!/usr/bin/env python3
""" Implements a function with duck annotation
"""
from typing import Iterable, Sequence, List, Tuple


def element_length(lst: Iterable[Sequence]) -> List[Tuple[Sequence, int]]:
    """ Returns the List of Tuples
    """
    return [(i, len(i)) for i in lst]
