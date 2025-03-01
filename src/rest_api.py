""""Launch a rest api for adding sounds"""

import threading
import os
import sys
import logging

import flask
from loguru import logger


class BotLogger(logging.Handler):
    def emit(self, record):
        logger_opt = logger.opt(depth=6, exception=record.exc_info)
        logger_opt.log(record.levelno, record.getMessage())


class RestApi(threading.Thread):
    """launch a flask server and take requests"""

    def __init__(self, play_queue, sound_dir, port):
        super().__init__()
        self._play_queue = play_queue
        self.flask_app = flask.Flask(__name__)

        """
        logger.add(
            sys.stderr,
            format="{time} {level} {message}",
            filter=__name__,
            level="DEBUG",
        )"""
        # logger.start(self.flask_app.config["LOGFILE"])
        self.flask_app.logger.addHandler(BotLogger())
        self._sound_dir = sound_dir
        self._port = port

        # add endpoints
        self.flask_app.add_url_rule("/", "index", self.serve_index)
        self.flask_app.add_url_rule(
            "/play/<path:clip_path>",
            "play",
            self.play_clip,
            methods=["POST"],
        )

    def serve_index(self):
        """servie index page"""
        sounds = self.get_sounds()
        return flask.render_template("index.jinja", sounds=sounds)

    def play_clip(self, clip_path):
        """add clip_path to queue"""
        # self._play_queue.put(os.path.join(self._sound_dir, clip_path))
        self._play_queue.put("/" + clip_path)
        return "success"

    def run(self):
        self.flask_app.run(
            host="0.0.0.0",
            port=self._port,
            debug=False,
        )

    def stop(self):
        """stop running flask"""
        self.flask_app.stop()

    def get_sounds(self):
        """get strucutred files"""
        sound_files = {}
        for root, _, files in os.walk(self._sound_dir):
            if len(files) > 0:
                dir_name = "/".join(root.split("/")[1:])
                sound_files[dir_name] = files

        return sound_files
