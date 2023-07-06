#!/usr/bin/env python3
"""
Module for task 7"""
from typing import Union, Tuple


def to_kv(k: str, v: Union[int, float]) -> Tuple[str, float]:
    """
    Type annotated function to return a tuple of a string and a float/integer
    from the input k of string and v of float/integer"""
    return (k, float(v**2))
