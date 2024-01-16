#!/usr/bin/env python3
"""Import async_comprehension from the previous file and
write a code that runs four parallel generations concurently and calculate
the time it takes to execute. Explain the reason for the time the program 
executes completely
"""


import time
import asyncio
async_comprehension = __import__('1-async_comprehension').async_comprehension


async def measure_runtime() -> float:
    """Measure the total runtime"""
    start_time = time.time()

    await asyncio.gather(*(async_comprehension() for i in range(4)))

    end_time = time.time()
    return end_time - start_time
