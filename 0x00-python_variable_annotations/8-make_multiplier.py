#!/usr/bin/env python3
'''Task 8's Module'''
from typing import Callable


def make_multiplier(multiplier: float) -> Callable[[float], float]:
    '''Returns a funtion for multiplier'''
    return lambda x: x * multiplier
