poly1 = [1, 2, 5]
poly2 = [2, 0, 1, -7]

def polyEval(poly, x):
    sum = 0 
    for i in range(0, len(poly), 1):
        sum += poly[i] * (x**i)
    return sum

def polySum(poly1, poly2):
    poly3 = []
    a = 0
    while (len(poly1)!=len(poly2)):
        if len(poly1)<len(poly2):
            poly1.append(0)
        else:
            poly2.append(0)
    for i in range(0, len(poly2), 1):
        a = poly1[i] + poly2[i]
        print(a)
        poly3.append(a)
    while poly3[-1] == 0:
        poly3.pop(-1)
    return poly3


def polyMultiply(poly1, poly2):
    poly3 = []
    lenPoly3 = len(poly1) + len(poly2) - 1
    a = 0
    for i in range(lenPoly3):
        poly3.append(0)
    for i in range(0, len(poly1), 1):
        for j in range(0, len(poly2), 1):
            a = poly1[i] * poly2[j]
            poly3[i+j] += a            
    return poly3
print(polyMultiply(poly1, poly2)) 

