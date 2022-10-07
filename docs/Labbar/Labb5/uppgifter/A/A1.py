import sys
sys.path.append("/home/jonalm/docs/Labbar/Labb5/lib/python3.10/site-packages/")
sys.path.append("/home/jonalm/docs/Labbar/Labb5/uppgifter/")

import numpy as np
import cv2
from cvlib import rgblist_to_cvimg

def cvimg_to_list(lst):
    """Returns a python list with tuples representing each pixel from OpenCV image"""
    python_lst = []

    for ele in lst:
        for sub_ele in ele:
            python_lst.append((sub_ele[0], sub_ele[1], sub_ele[2]))

    return python_lst

# img = cv2.imread("/home/jonalm/docs/Labbar/Labb5/images/flowers.jpg")

# list_img = cvimg_to_list(img)
# converted_img = rgblist_to_cvimg(list_img, img.shape[0], img.shape[1])

# cv2.imshow("converted", converted_img)
# cv2.waitKey(1000)