#!/usr/bin/env python3
'''Task 2's module.
'''
import asyncio
import time
async_comprehension = __import__('1-async_comprehension').async_comprehension


async def measure_runtime() -> float:
    """Run async_comprehension four times in parallel using asyncio.gather.
    measure_runtime should measure the total runtime and return it.
    Notice that the total runtime is roughly 10 seconds,
    explain it to yourself."""
    start = time.time()
    """The four async calls run in parallel so they take 10 seconds to
    complete, same as if a single async call was run"""
    await asyncio.gather(*(async_comprehension() for i in range(4)))
    # await asyncio.gather(async_comprehension())
    end = time.time()
    return end - start 
