import numpy as np

def FizzBuzz(start, finish):
    nums = np.arange(start, finish + 1)
    out = np.array(nums, dtype=object)

    mask3 = nums % 3 == 0
    mask5 = nums % 5 == 0
    mask15 = mask3 & mask5

    out[mask3] = "fizz"
    out[mask5] = "buzz"
    out[mask15] = "fizzbuzz"

    return out
