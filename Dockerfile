FROM debian: buster

RUN apt-get update && apt-get -y install \
	python3 \
	python3-git
	git 
	
RUN useradd --create-home -s /bin/bash bartender
ENV HOME /home/bartender
WORKDIR $HOME

RUN git clone https://github.com/xDDFF/discord-bot.git
RUN python3 -m pip install -U git+https://github.com/Rapptz/discord.py@rewrite#egg=discord.py \
		bs4 \
		requests
USER bartender
#RUN python3 bartender.py
