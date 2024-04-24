#!/usr/bin/env python3
'''
Python - Async Comprehension
'''
from typing import List
async_generator = __import__('0-async_generator').async_generator


async def async_comprehension() -> List[float]:
    """
    Coroutine that collects 10 random numbers using an async comprehension
    over the async_generator coroutine, then returns the 10 random numbers.
    """
    return [num async for num in async_generator()]
