import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation
import numpy as np

duration = 1  # second
fs = 44100
N = fs // 10
t = np.arange(np.ceil(duration * fs)) / fs

y1, y2, y3, y4 = -1.7, -1.8, -1.9, -2.0

f1 = 300

frequencies = np.linspace(10, 299, 500)

empty = np.ones_like(t) * np.nan

fig, (ax1, ax2) = plt.subplots(nrows=2, figsize=(16, 6))

ax1.plot([0, 1000/f1], [y1, y1], color='fuchsia', lw=4)
l12, = ax1.plot([None, None], [y2, y2], color='chartreuse', lw=4)
l13, = ax1.plot([None, None], [y3, y3], color='violet', lw=4)
l14, = ax1.plot([None, None], [y4, y4], color='brown', lw=4)

line1, = ax1.plot(t * 1000, empty)
ax1.set_xlim(t[0], t[-1] * 1000)
ax1.set_ylim(-2.1, 2.1)

ax2.plot([0, 1000/f1], [y1, y1], color='fuchsia', lw=4)
l22, = ax2.plot([None, None], [y2, y2], color='chartreuse', lw=4)
l23, = ax2.plot([None, None], [y3, y3], color='violet', lw=4)
l24, = ax2.plot([None, None], [y4, y4], color='brown', lw=4)

line2, = ax2.plot(t[:N] * 1000, empty[:N])
ax2.set_xlim(t[0], t[N - 1] * 1000)
ax2.set_ylim(-2.1, 2.1)
ax2.set_xlabel('time / ms')

constant_sine = np.sin(2 * np.pi * f1 * t)


def animate(f2):
    data = constant_sine + np.sin(2 * np.pi * f2 * t)
    l12.set_xdata([0, 1000/f2])
    l13.set_xdata([0, 1000*2/(f1+f2)])
    l14.set_xdata([0, 1000*2/(f1-f2)])
    line1.set_ydata(data)

    l22.set_xdata([0, 1000/f2])
    l23.set_xdata([0, 1000*2/(f1+f2)])
    l24.set_xdata([0, 1000*2/(f1-f2)])
    line2.set_ydata(data[:N])
    return line1, line2, l12, l13, l14, l22, l23, l24

ani = FuncAnimation(fig, animate, frequencies,
                    interval=50, blit=True, repeat=False)
plt.show()
