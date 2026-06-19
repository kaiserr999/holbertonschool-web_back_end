#!/usr/bin/env python3
"""
This module contains a coroutine that measures the total runtime of
executing an asynchronous comprehension four times in parallel.
"""

import asyncio
import time

# Import dynamique comme requis par le style de l'école
async_comprehension = __import__('1-async_comprehension').async_comprehension


async def measure_runtime() -> float:
    """
    Executes async_comprehension four times in parallel using asyncio.gather,
    measures the total execution time, and returns it.
    """
    start_time = time.perf_counter()

    # Exécution en parallèle des 4 coroutines
    await asyncio.gather(*(async_comprehension() for _ in range(4)))

    end_time = time.perf_counter()
    return end_time - start_time
