import sys
sys.path.append("/home/jonalm/docs/Labbar/Labb5/lib/python3.10/site-packages/")

import numpy as np
import cv2 as cv

def G(x, y, s = 4.5):
    if x == y == 0:
        return 1.5
    else:
        return "{:.6f}".format((-(1/(2*np.pi*s**2)))*np.exp(-(((x**2)+(y**2))/(2*s**2))))

def unsharp_mask(N):
    """"""
    array = []
    y = round((N//2)*-1)
    x = y - 1
    for ele in range(N):
        x =+ 1
        for sub_ele in range(N):
            array.append([G(x, y), G(x, y+1), G(x, y+2)])
    
    print("Array length:", len(array))
    return array


print(unsharp_mask(3))
# 
# array = [[x for x in range(2)] for y in range(N*N)]
print(G(0,-1))
