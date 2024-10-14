#!/usr/bin/env python3
""" Returns the delay on the in a list
"""
import asyncio
task_wait_random = __import__('3-tasks').wait_random


async def task_wait_n(n: int, max_delay: int) -> list:
    """ Spawns task_wait_random n times with specified max_delay
    and returns a list of delays.
    """
    tasks = [task_wait_random(max_delay) for _ in range(n)]
    delays = await asyncio.gather(*tasks)
    return sorted(delays)
