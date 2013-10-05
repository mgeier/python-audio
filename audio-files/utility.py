"""
Helper functions for working with audio files in NumPy.
"""

import numpy as np
import contextlib

def pcm2float(sig, dtype=np.float64):
    """
    Convert PCM signal to floating point with a range from -1 to 1.

    Use dtype=np.float32 for single precision.

    Parameters
    ----------
    sig : array_like
        Input array, must have (signed) integral type.
    dtype : data-type, optional
        Desired (floating point) data type.

    Returns
    -------
    ndarray
        normalized floating point data.

    See Also
    --------
    dtype

    """
    # TODO: allow unsigned (e.g. 8-bit) data

    sig = np.asarray(sig)  # make sure it's a NumPy array
    assert sig.dtype.kind == 'i', "'sig' must be an array of signed integers!"
    dtype = np.dtype(dtype)  # allow string input (e.g. 'f')

    # Note that 'min' has a greater (by 1) absolute value than 'max'!
    # Therefore, we use 'min' here to avoid clipping.
    return sig.astype(dtype) / dtype.type(-np.iinfo(sig.dtype).min)


@contextlib.contextmanager
def printoptions(*args, **kwargs):
    """
    Context manager for temporarily setting NumPy print options.

    See http://stackoverflow.com/a/2891805/500098
    """
    original = np.get_printoptions()
    try:
        np.set_printoptions(*args, **kwargs)
        yield
    finally:
        np.set_printoptions(**original)

