FROM andrewosh/binder-base

MAINTAINER Matthias Geier <Matthias.Geier@gmail.com>

USER root

# install OS packages
RUN apt-get update
RUN apt-get install -y libsndfile1 sndfile-programs sox libsox-fmt-all
RUN apt-get install -y vorbis-tools
RUN apt-get install -y python-audioread python3-audioread

USER main

# install Python libraries
RUN pip install soundfile
RUN /home/main/anaconda/envs/python3/bin/pip install soundfile
