#!/usr/bin/env python3
"""Write a type-annotated function sum_mixed_list which takes a mixture
of integers and floats as inputs and gives a float as output
"""

import typing


def sum_mixed_list(mxd_lst: typing.List[typing.Union[int, float]]) -> float:
    """Returns the sum of the list as a float"""
    return float(sum(mxd_lst))
