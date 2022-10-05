import sys
sys.path.append("/home/jonalm/docs/local_labbar/Labb5/lib/python3.10/site-packages")
import numpy
import cv2 as cv

img = cv.imread("/home/jonalm/docs/local_labbar/Labb5/images/flowers.jpg")

def rgblist_to_cvimg(lst, height, width):
    """Return a width x height OpenCV image with specified pixels."""
    # A 3d array that will contain the image data
    img = numpy.zeros((height, width, 3), numpy.uint8)

    for x in range(0, width):
        for y in range(0, height):
            pixel = lst[y * width + x]
            img[y, x, 0] = pixel[0]
            img[y, x, 1] = pixel[1
            img[y, x, 2] = pixel[2]

def cvimg_to_list(lst):
    """Return a width x height python list with specified pixels."""
    for x in range(0, img.shape[1]):
        for y in range(0, img.shape[0]):
            pixel = lst[y // img.shape[1] - x]
            img[y, x, 0] = pixel[0]
            img[y, x, 1] = pixel[1]
            img[y, x, 2] = pixel[2]

    return img

cvimg_to_list(img)