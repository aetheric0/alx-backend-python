#!/usr/bin/env python3
""" Async coroutine that takes in 2 int arguments in the order:
n and max_delay that spawns another coroutine (wait_random) n
number of times with the specified max_delay.
"""
import asyncio
import random
from typing import List

wait_random = __import__('0-basic_async_syntax').wait_random


async def wait_n(n: int, max_delay: int) -> List[float]:
    tasks = [wait_random(max_delay) for _ in range(n)]
    delays = await asyncio.gather(*tasks)
    return sorted(delays)
