""" RUN THE BOT """
import asyncio
import queue
import soundbot
import controller

# import testinput
import rest_api
import os
import dotenv


def main():
    """create and arun a bot"""
    dotenv.load_dotenv
    token = os.environ["TOKEN"]
    sound_requests = queue.Queue()
    loop = asyncio.get_event_loop()
    model_robot = soundbot.SoundBot(token, loop, "!AH")

    bot_control = controller.Controller(sound_requests, model_robot)
    bot_control.start()
    api_thread = rest_api.RestApi(sound_requests, "sounds")
    api_thread.start()
    asyncio.ensure_future(model_robot.start())
    loop.run_forever()

    loop.close()


if __name__ == "__main__":
    main()
