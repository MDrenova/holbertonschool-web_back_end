#!/usr/bin/env python3
import asyncio
import random
from typing import Generator
'''
Python - Async Comprehension
'''


async def async_generator() -> Generator[float, None, None]:
    """
    Coroutine that asynchronously waits for 1 second,
    then yields a random number between 0 and 10.
    """
    for _ in range(10):
        await asyncio.sleep(1)
        yield random.randint(0, 10)
