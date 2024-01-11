#!/usr/bin/env python3
"""Write a type-annotated function to_kv that takes a string and an integer as
input or a float as input and returns a tuple as answer
"""


import typing


def to_kv(k: str, v: typing.Union[int, float]) -> typing.Tuple[str, float]:
    """returns a tuple of the string & square of v as float"""
    return (k, float(v * v))
