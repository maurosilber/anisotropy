import numpy as np
import pywt

from . import anisotropy

uhaar = pywt.Wavelet(name="Unnormalized Haar",
                     filter_bank=[[1, 1], [-1, 1], [0.5, 0.5], [0.5, -0.5]])


def wavelet_denoise(par_int, per_int, thres, level):
    par_int_dec = pywt.swtn(par_int, uhaar, level=level)
    per_int_dec = pywt.swtn(per_int, uhaar, level=level)

    for current_level in range(len(par_int_dec)):
        ani = anisotropy.anisotropy_from_intensity(par_int, per_int)
        var_ani = anisotropy.anisotropy_variance_from_intensity(par_int, per_int)
        ani_dec = pywt.swtn(ani, uhaar, level=1, start_level=current_level)[0]
        var_ani_dec = pywt.swtn(var_ani, uhaar, level=1, start_level=current_level)[0]

        for key in par_int_dec[current_level].keys():
            if 'd' not in key:
                par_int, per_int = par_int_dec[current_level][key], per_int_dec[current_level][key]
            else:
                a_key = 'a' * len(key)
                Z = ani_dec[key] / np.sqrt(var_ani_dec[a_key])
                cond = np.abs(Z) < thres
                par_int_dec[current_level][key][cond] = 0
                per_int_dec[current_level][key][cond] = 0

    par_int_rec = pywt.iswtn(par_int_dec, uhaar)
    per_int_rec = pywt.iswtn(per_int_dec, uhaar)

    return par_int_rec, per_int_rec
