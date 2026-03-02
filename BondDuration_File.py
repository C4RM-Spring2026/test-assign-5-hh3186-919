import numpy as np
def getBondDuration(y, face, couponRate, m, ppy=1):
    n = m * ppy
    c = face * couponRate / ppy
    t = np.arange(1, n + 1)
    pvm = (1 + y / ppy) ** (-t)
    pv_coupon = coupon * np.sum(pvm)
    pv_face = face * (1 + y / ppy) ** (-n)
    pvcfsum = pv_coupon + pv_face
    cf = np.full(m * ppy, coupon)
    cf[-1] += face
    pv = cf * pvm
    weighted_t = t * pv
    Duration = np.sum(weighted_t) / pvcfsum
    duration = Duration / ppy
    return(duration)
