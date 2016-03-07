FROM andrewosh/binder-base

MAINTAINER Matthias Geier <Matthias.Geier@gmail.com>

# install OS packages
USER root

# deb-multimedia is needed for ffmpeg
RUN echo deb http://www.deb-multimedia.org jessie main non-free > /etc/apt/sources.list.d/deb-multimedia.list

RUN apt-get update
# trust deb-multimedia:
RUN apt-get install -y --force-yes deb-multimedia-keyring
# refresh again:
RUN apt-get update
RUN apt-get install -y libsndfile1 sndfile-programs sox libsox-fmt-all
RUN apt-get install -y vorbis-tools
RUN apt-get install -y fonts-humor-sans
RUN apt-get install -y ffmpeg
RUN apt-get install -y pypy

# install Python libraries
USER main

RUN pip install soundfile
RUN $HOME/anaconda2/envs/python3/bin/pip install soundfile
RUN pip install audioread
RUN $HOME/anaconda2/envs/python3/bin/pip install audioread
RUN pip install mpld3
RUN $HOME/anaconda2/envs/python3/bin/pip install mpld3
