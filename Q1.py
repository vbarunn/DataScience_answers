# P(X<Y) is integrating the probablity function with y range for 0-INF and x ranging 0-y

from scipy.integrate import dblquad
import numpy as np
import math


def func(y, x):
    return math.exp((-1)*x-y)


ans, err = dblquad(func, 0, math.inf,
                   lambda x: 0,
                   lambda x: math.exp(-2*x))
print(ans)