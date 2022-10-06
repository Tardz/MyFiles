import sys
sys.path.append("/home/jonalm/docs/Labbar/Labb5/lib/python3.10/site-packages/")
sys.path.append("/home/jonalm/docs/Labbar/Labb5/uppgifter/")

import numpy as np
import cv2
from A.A1 import cvimg_to_list
from cvlib import rgblist_to_cvimg

def generator_from_image(img):
    """Returns a func which returns the color of a given index"""
    
    return (
        lambda index: img[index] 
    )

# orig_img = cv2.imread("/home/jonalm/docs/Labbar/Labb5/images/plane.jpg")
# orig_list = cvimg_to_list(orig_img)

# generator = generator_from_image(orig_list)

# new_list = [generator(i) for i in range(len(orig_list))]

# cv2.imshow('original', orig_img)
# cv2.imshow('new', rgblist_to_cvimg(new_list, orig_img.shape[0], orig_img.shape[1]))
# cv2.waitKey(0)

