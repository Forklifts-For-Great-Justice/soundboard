"""Discord bot to connect to discord and play sound clips"""

import time
import discord
import bot


class SoundBot(bot.Bot):
    """
    Wait for events to play sounds
    """

    # async def play_clip(self, clip_path):
    def play_clip(self, clip_path):
        """Play the specified soundclip"""
        print("playing", clip_path)
        voice_client = self.client.voice_clients[0]
        sound = discord.FFmpegPCMAudio(clip_path)
        voice_client.play(sound)
        while voice_client.is_playing():
            # await asyncio.sleep(1)
            time.sleep(1)

    async def on_ready(self):
        print("SoundBot online")
        for channel in self.client.get_all_channels():
            if channel.name == "Forklift Voice":
                print("Joining voice channel")
                await channel.connect()
                print("Voice joined")
