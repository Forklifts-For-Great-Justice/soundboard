""" Generic Bot class to handle bot things """
from datetime import datetime
import discord
import command

class Bot():
    """ Bot class, for bots """
    def __init__(self, token, loop, prefix):
        self.client = discord.Client(loop=loop, intents=discord.Intents.default())
        self.commands = dict()
        self.prefix = prefix
        self.token = token
        self._start_time = datetime.now()

        # add event handlers
        self.client.event(self.on_member_update)
        self.client.event(self.on_message)
        self.client.event(self.on_ready)

        # register commands
        self._add_commands()

    async def on_message(self, message):
        """ message handling function"""

    async def on_ready(self):
        """ on ready handler"""

    async def on_member_update(self, old, new):
        """ member update handler"""

    async def start(self):
        """ login in to discord and wait for events"""
        await self.client.login(self.token)
        await self.client.connect()

    def add_command(self, *args, **kwargs):
        """
        add a command to the bot
        """
        cmd = command.Command(*args, **kwargs)
        self.commands[cmd.name] = cmd
        print("adding command: {}".format(cmd.name))

    def _add_commands(self):
        """
        add all commands
        """
