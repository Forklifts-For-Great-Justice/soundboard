FROM	python:3.12-bullseye

WORKDIR	/srv
COPY	src	.
COPY	requirements.txt	.
RUN	apt update \
	&& apt install -y ffmpeg
RUN	pip  install -r /srv/requirements.txt
ENV	TOKEN	"CHANGEME"
ENV	SOUNDS	"/sounds"
CMD	["python3","main.py"]
