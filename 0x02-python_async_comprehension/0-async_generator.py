#!/usr/bin/env python3
"""Write a coroutine called async_generator that takes no arguments.
The program loops ten times and for each loop produces a result waits
for a given time and goes to the next loop
"""


import asyncio
import random
from typing import Generator


async def async_generator() -> Generator[float, None, None]:
    """Loop 10 times, wait 1 sec each time before the next loop"""
    for i in range(10):
        await asyncio.sleep(1)
        yield random.random() * 10
