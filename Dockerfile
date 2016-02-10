FROM andrewosh/binder-base

MAINTAINER Matthias Geier <Matthias.Geier@gmail.com>

USER root

# install OS packages
RUN apt-get update
RUN apt-get install -y libsndfile1 sndfile-programs sox libsox-fmt-all
RUN apt-get install -y vorbis-tools
RUN apt-get install -y fonts-humor-sans

USER main

# install Python libraries
RUN pip install soundfile
RUN $HOME/anaconda2/envs/python3/bin/pip install soundfile
RUN pip install audioread
RUN $HOME/anaconda2/envs/python3/bin/pip install audioread
RUN pip install mpld3
RUN $HOME/anaconda2/envs/python3/bin/pip install mpld3
