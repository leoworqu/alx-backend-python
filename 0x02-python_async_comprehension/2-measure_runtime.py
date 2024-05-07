#!/usr/bin/env python3
""" coroutine that will execute async_comprehension four times in parallel """

import asyncio
import random
import timeit
async_comprehension = __import__('1-async_comprehension').async_comprehension


async def measure_runtime() -> float:
    """ executes comprehension func 4 times in parallel, returns runtime """

    start = timeit.default_timer()
    await asyncio.gather(
        async_comprehension(),
        async_comprehension(),
        async_comprehension(),
        async_comprehension()
        )
    stop = timeit.default_timer()
    return stop - start
