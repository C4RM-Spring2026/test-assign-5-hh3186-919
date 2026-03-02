import numpy as np
def getBondPrice(y, face, couponRate, m, ppy=1):
    n = m * ppy
    coupon = face * couponRate / ppy
    t = np.arange(1, n + 1)
    pvm = (1 + y / ppy) ** (-t)
    pv_coupon = coupon * np.sum(pvm)
    pv_face = face * (1 + y / ppy) ** (-n)
    bondprice = pv_coupon + pv_face
    return(bondprice)
