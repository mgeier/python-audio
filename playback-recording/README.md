Audio Playback and Recording
============================

[back to main page](../README.md)

This is work-in-progress!

There are several libraries for audio playback and/or recording available for
Python.
They greatly differ in features, API, requirements, quality, ...

### PySoundCard

https://github.com/bastibe/PySoundCard

uses PortAudio via CFFI

### PyAudio

bindings for PortAudio

http://people.csail.mit.edu/hubert/pyaudio/

### pygame.mixer

uses [SDL](http://www.libsdl.org/)

http://pygame.org/docs/ref/mixer.html

Debian package: python-pygame

### pyglet

http://pyglet.org

DirectSound on Windows, ALSA on Linux, OpenAL on Windows/Linux/MacOSX: http://www.pyglet.org/doc/programming_guide/audio_drivers.html

Debian package: python-pyglet

Many codecs supported with [AVbin](http://code.google.com/p/avbin/).

Debian package: libavbin0 and/or libavbin-dev?

### pySFML

http://python-sfml.org/examples.html

Debian packages python-sfml and python3-sfml.

Uses [OpenAL Soft][] for playback/recording and
[libsndfile][] for audio file handling.

[OpenAL Soft]: http://kcat.strangesoft.net/openal.html
[libsndfile]: http://www.mega-nerd.com/libsndfile/

### Snack

Depends on Tkinter

http://www.speech.kth.se/snack/  
http://www.speech.kth.se/snack/man/snack2.2/python-man.html

Debian package: libsnack2-alsa

no new releases since December 2005!

### PyAudiere!

http://pyaudiere.org/

uses audiere: http://audiere.sourceforge.net/

### audioloop

standard Python lib to manipulate raw audio data

http://docs.python.org/library/audioop.html

### PySndObj

platform independent, including JACK!

http://sndobj.sourceforge.net/

### PyJack

http://sourceforge.net/projects/py-jack/

### medussa

http://www.medussa.us  
https://code.google.com/p/medussa/

### py-portaudio

https://github.com/ranweiler/py-portaudio

<!--
vim:textwidth=80
-->
