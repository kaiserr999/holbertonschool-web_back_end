#!/usr/bin/env python3
"""
This module contains an asynchronous generator coroutine that loops
10 times, waits 1 second asynchronously per iteration, and yields
a random float number between 0 and 10.
"""

import asyncio
import random
from typing import Generator


async def async_generator() -> Generator[float, None, None]:
    """
    Asynchronously loops 10 times, pausing for 1 second each time,
    and yields a random floating-point number between 0 and 10.
    """
    for _ in range(10):
        await asyncio.sleep(1)
        yield random.uniform(0, 10)
