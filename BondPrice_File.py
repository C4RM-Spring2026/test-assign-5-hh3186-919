import numpy as np

def getBondPrice(y, face, couponRate, m, ppy=1):
    
    r = y / ppy
    n = m * ppy
    c = face * couponRate / ppy
  
    t = np.arange(1, n + 1)
    
    discount = 1 / (1 + r) ** t
    
    cashflows = np.full(n, c)
    cashflows[-1] += face
    
    price = np.sum(cashflows * discount)
    
    return price
