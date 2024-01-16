#!/usr/bin/env python3
"""Write an asynchronous coroutine that takes in an integer argument
(max_delay, with a default value of 10) and returns the result after
waiting for the randomly selected delay period
"""


import random
import asyncio


async def wait_random(max_delay: int = 10) -> float:
    """Wait for a randomly selected time"""
    wait_time = random.random() * max_delay
    await asyncio.sleep(wait_time)
    return wait_time
