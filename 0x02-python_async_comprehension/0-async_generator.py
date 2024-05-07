#!/usr/bin/env python3
""" a coroutine called async_generator that takes no arguments. """

from typing import Generator
import asyncio
import random


async def async_generator() -> Generator[float, None, None]:
    """ The coroutine will loop 10 times, each time asynchronously wait 1 second """

    for i in range(10):
        yield random.random()
        await asyncio.sleep(1)
