#!/usr/bin/env python3
'''Task's 1 modules'''
import asyncio
from typing import List
ran_delay = __import__('0-basic_async_syntax').wait_random


async def wait_n(n: int, max_delay: int) -> List[float]:
    '''Iterate the ran_delay n times'''
    waiting = await asyncio.gather(
        *tuple(map(lambda _: ran_delay(max_delay), range(n)))
    )
    return sorted(waiting)
