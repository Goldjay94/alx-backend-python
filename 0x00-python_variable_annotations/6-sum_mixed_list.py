#!/usr/bin/env python3
"""
Module for task 6"""
from typing import Union, List


def sum_mixed_list(mxd_lst: List[Union[int, float]]) -> float:
    """
    Type annotated function to return the sum of a list of
    floats or/and ints"""
    return sum(mxd_lst)
