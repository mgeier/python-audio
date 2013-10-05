#!/usr/bin/env python
# vim:fileencoding=utf-8:softtabstop=4:shiftwidth=4:expandtab:textwidth=80

from __future__ import division
import numpy as np
from scikits.audiolab import Sndfile, Format
from contextlib import closing

formats = ('wav', 'wavex')
encodings = ('pcm16', 'pcm24', 'float32')
fs = 44100  # sampling rate
ch = 7  # number of audio channels

# column vector
x = np.linspace(0, 2 * np.pi, ch * 2 + 1).reshape(-1, 1)

n = np.arange(ch)  # partial tones

# a funny multichannel signal including 1 and -1 to show potential clipping
sig = np.cos((n + 1) * x) * (1 - n / ch)

for format in formats:
    for encoding in encodings:
        filename = 'test_%(format)s_%(encoding)s.wav' % locals()
        fmt = Format(format, encoding)
        with closing(Sndfile(filename, 'w', fmt, sig.shape[1], fs)) as f:
            f.write_frames(sig)
