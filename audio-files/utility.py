"""Helper functions for working with audio files in NumPy."""

import numpy as np
import contextlib


def pcm2float(sig, dtype='float64'):
    """Convert PCM signal to floating point with a range from -1 to 1.

    Use dtype='float32' for single precision.

    Parameters
    ----------
    sig : array_like
        Input array, must have (signed) integral type.
    dtype : data type, optional
        Desired (floating point) data type.

    Returns
    -------
    ndarray
        normalized floating point data.

    See Also
    --------
    float2pcm, dtype

    """
    # TODO: allow unsigned (e.g. 8-bit) data

    sig = np.asarray(sig)
    if sig.dtype.kind != 'i':
        raise TypeError("'sig' must be an array of signed integers")
    dtype = np.dtype(dtype)
    if dtype.kind != 'f':
        raise TypeError("'dtype' must be floating point type")

    # Note that 'min' has a greater (by 1) absolute value than 'max'!
    # Therefore, we use '-min' here to avoid clipping.
    return sig.astype(dtype) / dtype.type(-np.iinfo(sig.dtype).min)


def float2pcm(sig, dtype='int16'):
    """Convert floating point signal with a range from -1 to 1 to PCM.

    Parameters
    ----------
    sig : array_like
        Input array, must have floating point type.
    dtype : data type, optional
        Desired (integer) data type.

    Returns
    -------
    ndarray
        integer data.

    See Also
    --------
    pcm2float, dtype

    """
    # TODO: allow unsigned (e.g. 8-bit) data

    sig = np.asarray(sig)
    if sig.dtype.kind != 'f':
        raise TypeError("'sig' must be a float array")
    dtype = np.dtype(dtype)
    if dtype.kind != 'i':
        raise TypeError("'dtype' must be signed integer type")

    return (sig * np.iinfo(dtype).max).astype(dtype)


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
        The content of `data` converted to an `int32` array, where each
        value was padded with zero-bits in the least significant byte
        (`normalize=True`) or in the most significant byte
        (`normalize=False`).

    """
    if len(data) % 3 != 0:
        raise ValueError("Size of data must be a multiple of 3 bytes")

    out = np.zeros(len(data) // 3, dtype='<i4')
    out.shape = -1, channels
    temp = out.view('uint8').reshape(-1, 4)
    if normalize:
        # write to last 3 columns, leave LSB at zero
        columns = slice(1, None)
    else:
        # write to first 3 columns, leave MSB at zero
        columns = slice(None, -1)
    temp[:, columns] = np.frombuffer(data, dtype='uint8').reshape(-1, 3)
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
