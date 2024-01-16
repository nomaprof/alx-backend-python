#!/usr/bin/env python3
"""Import wait_random from 0-basic_async_syntax and write a normal
python program that returns a asyncio.Task
"""


import asyncio
wait_random = __import__('0-basic_async_syntax').wait_random


def task_wait_random(max_delay: int) -> asyncio.Task:
    """Returns a asyncio.Task using a normal python code"""
    return asyncio.create_task(wait_random(max_delay))
