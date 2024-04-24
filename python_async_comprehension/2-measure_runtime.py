#!/usr/bin/env python3
import asyncio
import time
'''
Python - Async Comprehension
'''

async_comprehension = __import__('1-async_comprehension').async_comprehension


async def measure_runtime():
    """
    Coroutine that executes async_comprehension four times in parallel,
    measures the total runtime, and returns it.
    """
    start = time.time()
    await asyncio.gather(*(async_comprehension() for _ in range(4)))
    end = time.time()
    return end - start
