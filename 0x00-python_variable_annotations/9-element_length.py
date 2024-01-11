#!/usr/bin/env python3
"""Annotate the below function’s parameters with the proper
types and ensure the result is the correct type
"""


import typing


def element_length(lst: typing.Iterable[typing.Sequence]) -> \
        typing.List[typing.Tuple[typing.Sequence, int]]:
    """Returns a list of tuples"""
    return [(i, len(i)) for i in lst]
