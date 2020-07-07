import math

def newtonPi(init):
    x_new = init
    condition = True
    while condition:
        x_old = x_new
        x_new = x_old - (math.sin(x_old)/math.cos(x_old))
        condition = x_new != x_old
    return x_new



def leibnizPi(iterations):
    amount = 0.0
    sign = 1
    for k in range(1, iterations+1):
        amount += 4*sign/(2*k - 1)
        sign = sign *(-1)
    return amount


def nilakanthaPi(iterations):
    amount = 0.0
    sign = 1
    if iterations == 1:
        amount = 0.0
    else:
        for k in range(1, iterations):
            amount += (4*sign)/((2*k)*(2*k+1)*(2*k+2))
            sign = sign *(-1)
    return (3 + amount)