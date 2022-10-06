import sys
sys.path.append("/home/jonalm/docs/Labbar/Labb5/lib/python3.10/site-packages/")

import numpy as np
import cv2 as cv

def G(y, x, s = 4.5):
    """
    Formula for gaussian blur, returns negative value except for 
    position (0,0) which returns 1,5.
    """
    if x == y == 0:
        return 1.5
    else:
        return (-(1/(2*np.pi*s**2)))*np.exp(-(((x**2)+(y**2))/(2*s**2)))

def unsharp_mask(N):
    """
    Returns a 2D list of length N*N. Each element in the list contains its
    gaussian blur value for that specified position.
    """
    array = [[ele for ele in range(N)] for ele in range(N*N)]
    y = round((N//2)*-1) - 1
    
    for lst in array:
        x = round((N//2)*-1)
        y += 1
        for num in lst:
            lst[num] = G(y, x)
            x += 1
    
    return array

img = cv.imread("/home/jonalm/docs/Labbar/Labb5/images/flowers_to_greyscale.jpg")
kernel = np.array(unsharp_mask(100))
filtered_img = cv.filter2D(img, -1, kernel)
cv.imshow("sharp_flowers", filtered_img)
cv.waitKey(0)
