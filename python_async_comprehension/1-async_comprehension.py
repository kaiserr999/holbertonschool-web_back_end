#!/usr/bin/env python3
"""
This module contains a coroutine that uses an asynchronous comprehension
to collect 10 random numbers from an asynchronous generator.
"""

from typing import List

# Import dynamique comme requis par le style de l'école
async_generator = __import__('0-async_generator').async_generator


async def async_comprehension() -> List[float]:
    """
    Collects 10 random float numbers asynchronously using an async
    comprehension over async_generator and returns the list of numbers.
    """
    return [i async for i in async_generator()]
