def total_intensity(par_int, per_int):
    """Calculate total intensity from parallel and perpendicular intensity.

    Parameters
    ----------
    par_int: Parallel intensity component.
    per_int: Perpendicular intensity component.
    """
    return par_int + 2 * per_int


def anisotropy_from_intensity(par_int, per_int, ret_total_int=False):
    """Calculates anisotropy from parallel and perpendicular intensity.

    Parameters
    ----------
    par_int: Parallel intensity component.
    per_int: Perpendicular intensity component.
    ret_total_int: bool
        If True, returns (anisotropy, total intensity) tuple
    """
    total_int = total_intensity(par_int, per_int)
    ani = (par_int - per_int) / total_int
    return (ani, total_int) if ret_total_int else ani


def intensity_from_anisotropy(ani, total_int):
    """Calculates parallel and perpendicular intensities from total intensity and anisotropy.

    Parameters
    ----------
    ani: anisotropy
    total_int: total intensity

    Returns
    -------
    tuple (par_int, per_int)
        - par_int: Parallel intensity component.
        - per_int: Perpendicular intensity component.
    """
    par_int = total_int / 3 * (1 + 2 * ani)
    per_int = total_int / 3 * (1 - ani)
    return par_int, per_int


def anisotropy_variance_from_intensity(par_int, per_int):
    """Calculates variance of anisotropy from parallel and perpendicular intensities
    assuming Poisson statistics.

    Parameters
    ----------
    par_int: Parallel intensity component.
    per_int: Perpendicular intensity component.

    """
    return 9 * (par_int + per_int) * par_int * per_int / (par_int + 2 * per_int) ** 4
