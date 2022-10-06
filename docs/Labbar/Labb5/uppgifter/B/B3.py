import sys
sys.path.append("/home/jonalm/docs/Labbar/Labb5/lib/python3.10/site-packages/")
sys.path.append("/home/jonalm/docs/Labbar/Labb5/uppgifter/")

import numpy as np
import cv2
import random
from A.A1 import cvimg_to_list
from B.B1 import pixel_constraint
from B.B2 import generator_from_image

def generator1(index):
    val = random.random() * 255 if random.random() > 0.99 else 0
    return (val, val, val)

def combine_images(hsv_list, condition, generator1, generator2):
    return True

plane_img = cv2.imread("/home/jonalm/docs/Labbar/Labb5/images/plane.jpg")

condition = pixel_constraint(100, 150, 50, 200, 100, 255)

hsv_list = cvimg_to_list(cv2.cvtColor(plane_img, cv2.COLOR_BGR2HSV))
plane_img_list = cvimg_to_list(plane_img)