import numpy as np

def getBondDuration(y, face, couponRate, m, ppy=1):
    r = y / ppy
    n = m*ppy
    c = face * couponRate / ppy

    t = np.arange(1, n + 1, dtype=float)
    disc = (1.0 + r) ** (-t)

    cf = np.full(int(n), c, dtype=float)
    cf[-1] += face

    pvcf = cf * disc
    price = np.sum(pvcf)

    dur = np.sum(t * pvcf) / price
    return dur / ppy
