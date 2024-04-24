#!/usr/bin/env python3
import asyncio
import random
'''
Python - Async Comprehension
'''


async def async_generator():
    """
    Coroutine that asynchronously waits for 1 second,
    then yields a random number between 0 and 10.
    """
    for _ in range(10):
        await asyncio.sleep(1)
        yield random.randint(0, 10)
