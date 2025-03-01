""" Class to handle loading new commands for the bot """

import re
import asyncio

import loguru


class Command:  # pylint: disable=too-few-public-methods
    """Class to handle loading new commands for the bot"""

    def __init__(self, name: str, handler, regexp=r""):
        self.name = name
        self.regexp = re.compile(regexp) if regexp else None
        if not asyncio.iscoroutine(handler):
            loguru.info("All commands must be coroutines")
            handler = asyncio.coroutine(handler)
        self.handler = handler
        self.help = handler.__doc__ or ""

    async def call(self, message: str):
        """check if message matches regex and call"""
        data = " ".join(message.content.split()[2:])
        if self.regexp:
            match = self.regexp.match(data)
            if not match:
                return
            await self.handler(message, **match.groupdict())
        else:
            await self.handler(message)
