"""Discord bot to connect to discord and play sound clips"""

import time

import discord
from loguru import logger

import bot


class SoundBot(bot.Bot):
    """
    Wait for events to play sounds
    """

    # async def play_clip(self, clip_path):
    def play_clip(self, clip_path):
        """Play the specified soundclip"""
        logger.info(f"playing: {clip_path}")
        voice_client = self.client.voice_clients[0]
        sound = discord.FFmpegPCMAudio(clip_path)
        voice_client.play(sound)
        while voice_client.is_playing():
            # await asyncio.sleep(1)
            time.sleep(1)

    async def on_ready(self):
        logger.info("SoundBot online")
        for channel in self.client.get_all_channels():
            if channel.name == "Forklift Voice":
                logger.info("Joining voice channel")
                await channel.connect()
                logger.info("Voice joined")
