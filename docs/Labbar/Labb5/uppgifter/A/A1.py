import sys
sys.path.append("/home/jonalm/docs/Labbar/Labb5/lib/python3.10/site-packages/")

import numpy as np
import cv2

def rgblist_to_cvimg(lst, height, width):
    """Return a width x height OpenCV image with specified pixels."""
    # A 3d array that will contain the image data
    img = np.zeros((height, width, 3), np.uint8)

    for x in range(0, width):
        for y in range(0, height):
            pixel = lst[y * width + x]
            img[y, x, 0] = pixel[0]
            img[y, x, 1] = pixel[1]
            img[y, x, 2] = pixel[2]
    
    return img

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