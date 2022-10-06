import sys
sys.path.append("/home/jonalm/docs/Labbar/Labb5/lib/python3.10/site-packages/")
sys.path.append("/home/jonalm/docs/Labbar/Labb5/uppgifter/")

import numpy as np
import cv2
from A.A1 import cvimg_to_list
from cvlib import greyscale_list_to_cvimg

def pixel_constraint(hlow, hhigh, slow, shigh, vlow, vhigh):
    """
    Returns a func which returns 1 if the color values 
    of a pixel is between the set boundaries, else 0.
    """

    return (
            lambda pixels: 1 if 
            hlow < pixels[0] < hhigh and 
            slow < pixels[1] < shigh and 
            vlow < pixels[2] < vhigh else 0
            )

# hsv_plane = cv2.cvtColor(cv2.imread("/home/jonalm/docs/Labbar/Labb5/images/plane.jpg"), cv2.COLOR_BGR2HSV)
# plane_list = cvimg_to_list(hsv_plane)

# is_sky = pixel_constraint(100, 150, 50, 200, 100, 255)
# sky_pixels = list(map(lambda x: x * 255, map(is_sky, plane_list)))

# cv2.imshow('sky', greyscale_list_to_cvimg(sky_pixels, hsv_plane.shape[0], hsv_plane.shape[1]))
# cv2.waitKey(0)