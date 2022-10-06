import sys
sys.path.append("/home/jonalm/docs/Labbar/Labb5/lib/python3.10/site-packages/")

import numpy as np
import cv2 as cv

def pixel_constraint(hlow, hhigh, slow, shigh, vlow, vhigh):
    """
    Returns 1 if the color values of a pixel or list of pixels are 
    Between the set boundaries, else 0.
    """

    def func(tuple_pixel_or_list_of_pixels):
        return x, y, z
        
    return func(tuple_pixel_or_list_of_pixels)




    



is_black = pixel_constraint(0, 255, 0, 255, 0, 10)
print(is_black((231, 82, 4)))




    # return (lambda x, y, z, pixel_lst = []: pixel_lst.append(1) if 
    # hlow < x < hhigh and slow < y < shigh and vlow < z < vhigh 
    # else pixel_lst.append(0))

# def pixel_constraint(hlow, hhigh, slow, shigh, vlow, vhigh):
#     """
#     Returns 1 if the color values of a pixel or list of pixels are 
#     Between the set boundaries, else 0.
#     """
#     lst = []
#     return (lambda x: 1 if 
#                     hlow < x[0] < hhigh and 
#                     slow < x[1] < shigh and 
#                     vlow < x[2] < vhigh and 
#                     type(x) == tuple else 
#                     (lst if 
#                     hlow < x[0][0] < hhigh and
#                     slow < x[0][1] < shigh and 
#                     vlow < x[0][2] < vhigh 
#                     else 0 ))