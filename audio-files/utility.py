"""Helper functions for working with audio files in NumPy."""

import contextlib
import numpy as np


def pcm2float(sig, dtype="float64"):
    """Convert PCM signal to floating point with a range from -1 to 1.

    Use dtype='float32' for single precision.

    >>> import numpy as np
    >>> sig = np.array([-32768, 0, 32767], dtype='int16')
    >>> pcm2float(sig, 'float64')
    array([-1.        ,  0.        ,  0.99996948])

    Parameters
    ----------
    sig : array_like
        Input array, must have integral type.
    dtype : data type, optional
        Desired (floating point) data type.

    Returns
    -------
    numpy.ndarray
        Normalized floating point data.

    See Also
    --------
    float2pcm, dtype

    """
    sig = np.asarray(sig)
    if sig.dtype.kind not in "iu":
        raise TypeError("'sig' must be an array of integers")
    dtype = np.dtype(dtype)
    if dtype.kind != "f":
        raise TypeError("'dtype' must be a floating point type")

    i = np.iinfo(sig.dtype)
    abs_max = 2 ** (i.bits - 1)
    offset = i.min + abs_max
    return (sig.astype(dtype) - offset) / abs_max


def float2pcm(sig, dtype="int16"):
    """Convert floating point signal with a range from -1 to 1 to PCM.

    Any signal values outside the interval [-1.0, 1.0) are clipped.
    No dithering is used.

    >>> import numpy as np
    >>> sig = np.array([-1.0, 0.0, 0.5], dtype='float64')
    >>> float2pcm(sig, 'int16')
    array([-32768,      0,  16384], dtype=int16)

    Parameters
    ----------
    sig : array_like
        Input array, must have floating point type.
    dtype : data type, optional
        Desired (integer) data type.

    Returns
    -------
    numpy.ndarray
        Integer data, scaled and clipped to the range of the given
        *dtype*.

    See Also
    --------
    pcm2float, dtype

    """
    sig = np.asarray(sig)
    if sig.dtype.kind != "f":
        raise TypeError("'sig' must be a float array")
    dtype = np.dtype(dtype)
    if dtype.kind not in "iu":
        raise TypeError("'dtype' must be an integer type")

    i = np.iinfo(dtype)
    abs_max = 2 ** (i.bits - 1)
    offset = i.min + abs_max
    return (sig * abs_max + offset).clip(i.min, i.max).astype(dtype)


def pcm24to32(data, channels=1, normalize=True):
    """Convert 24-bit PCM data to 32-bit.

    Parameters
    ----------
    data : buffer
        A buffer object where each group of 3 bytes represents one
        little-endian 24-bit value.
    channels : int, optional
        Number of channels, by default 1.
    normalize : bool, optional
        If ``True`` (the default) the additional zero-byte is added as
        least significant byte, effectively multiplying each value by
        256, which leads to the maximum 24-bit value being mapped to the
        maximum 32-bit value.  If ``False``, the zero-byte is added as
        most significant byte and the values are not changed.

    Returns
    -------
    numpy.ndarray
        The content of *data* converted to an *int32* array, where each
        value was padded with zero-bits in the least significant byte
        (``normalize=True``) or in the most significant byte
        (``normalize=False``).

    """
    if len(data) % 3 != 0:
        raise ValueError("Size of data must be a multiple of 3 bytes")

    out = np.zeros(len(data) // 3, dtype="<i4")
    out.shape = -1, channels
    temp = out.view("uint8").reshape(-1, 4)
    if normalize:
        # write to last 3 columns, leave LSB at zero
        columns = slice(1, None)
    else:
        # write to first 3 columns, leave MSB at zero
        columns = slice(None, -1)
    temp[:, columns] = np.frombuffer(data, dtype="uint8").reshape(-1, 3)
    return out


@contextlib.contextmanager
def printoptions(*args, **kwargs):
    """Context manager for temporarily setting NumPy print options.

    See http://stackoverflow.com/a/2891805/500098

    """
    original = np.get_printoptions()
    try:
        np.set_printoptions(*args, **kwargs)
        yield
    finally:
        np.set_printoptions(**original)


if __name__ == "__main__":
    import doctest

    doctest.testmod()
