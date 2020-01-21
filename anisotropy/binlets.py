from binlets import binlet

from . import functions

_my_binlet = binlet(functions.anisotropy_from_intensity,
                    functions.anisotropy_variance_from_intensity,
                    is_scalar=True)


def binlet_denoise(par_int, per_int, levels, p_value=0.05, **kwargs):
    """

    Parameters
    ----------
    par_int, per_int : numpy.ndarray
       Parallel and perpendicular intensities.
    levels : int
    p_value : float

    Returns
    -------
    par_int, per_int : numpy.ndarray
       Binned parallel and perpendicular intensities.
    """
    return _my_binlet((par_int, per_int), levels, p_value=p_value, **kwargs)
