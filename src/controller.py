"""Object to consume queue events and send request to the bot"""

import threading

from loguru import logger


class Controller(threading.Thread):
    """Consume queue events and have the discord bot play sounds"""

    def __init__(self, input_queue, soundbot):
        super().__init__()
        self._input_queue = input_queue
        self._soundbot = soundbot
        self._running = True

    def run(self):
        """main loop for thread"""
        logger.info("controller starting")
        while self._running:
            sound_request = self._input_queue.get()
            self._soundbot.play_clip(sound_request)

    def stop(self):
        """stop function"""
        self._running = False
