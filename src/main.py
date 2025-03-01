""" RUN THE BOT """

import asyncio
import queue
import os

import dotenv
from loguru import logger

import soundbot
import controller
import rest_api


def main():
    """create and arun a bot"""
    dotenv.load_dotenv()
    token = os.environ["TOKEN"]
    sound_root = os.environ["SOUNDS"]
    port = os.environ["PORT"]
    logger.info(f"sound_root is: {sound_root}")
    logger.info(f"token is: {token}")
    logger.info(f"port is: {port}")

    sound_requests = queue.Queue()
    loop = asyncio.get_event_loop()
    model_robot = soundbot.SoundBot(token, loop, "!AH")

    bot_control = controller.Controller(sound_requests, model_robot)
    bot_control.start()
    api_thread = rest_api.RestApi(sound_requests, sound_root, port)
    api_thread.start()
    asyncio.ensure_future(model_robot.start())
    try:
        loop.run_forever()
    except KeyboardInterrupt:
        logger.info("Stopping")
        loop.stop()
        bot_control.stop()
        api_thread.stop()

    loop.close()


if __name__ == "__main__":
    main()
