import sys
sys.path.append("/home/jonalm/docs/Labbar/Labb5/lib/python3.10/site-packages/")

import numpy as np
import cv2 as cv

def G(x, y, s = 4.5):
    return ((-(1//(2*np.pi*s**2)))*np.exp(-((x**2)+(y**2))//(2*s**2)))

def unsharp_mask(N):
    """"""
    N_index = round((N//2)*-1)

    array = [ele = for ele in range(N)]

print(unsharp_mask(3))

