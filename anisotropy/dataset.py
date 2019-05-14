from . import anisotropy


class Anisotropy:
    def __init__(self, par_int, per_int):
        self.par_int = par_int
        self.per_int = per_int

    @classmethod
    def from_filenames(cls, filenames):
        raise NotImplementedError

    def anisotropy(self):
        return anisotropy.anisotropy_from_intensity(self.par_int, self.per_int)

    def total_intensity(self):
        return anisotropy.total_intensity(self.par_int, self.per_int)

    def anisotropy_variance(self):
        return anisotropy.anisotropy_variance_from_intensity(self.par_int, self.per_int)
