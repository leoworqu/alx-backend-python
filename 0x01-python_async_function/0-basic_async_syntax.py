#!/usr/bin/env python3
"""
Asynchronous coroutine that waits for a random delay
Returns:
float: Random delay in seconds
"""


import asyncio
import random

async def wait_random(max_delay=10):
    """
    Asynchronous coroutine that waits for a random delay 
    Returns:
        float: Random delay in seconds.
    """
    delay = random.uniform(0, max_delay)
    await asyncio.sleep(delay)
    return delay

async def main():
    """
    Main asynchronous function that calls wait_random() and prints the delay.
    """
    delay = await wait_random()

asyncio.run(main())
